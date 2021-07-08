import logging
import telegram as tg

from config import *
from libgen_api import LibgenSearch


class GenesisBot:
    def __init__(self):
        self.main_menu =[
                            [tg.InlineKeyboardButton('Search By Title 🔍', switch_inline_query_current_chat='title '), tg.InlineKeyboardButton('Search By Author 🔎', switch_inline_query_current_chat='author ')],
                            [tg.InlineKeyboardButton('Cancel Op ❌', callback_data='cancel')]
                        ]

        self.library = LibgenSearch()
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __str__(self):
        return "Genesis, is a helper telegram bot which can download books off Library Genesis."

    def start(self, update, context):
        reply_markup = tg.InlineKeyboardMarkup(self.main_menu)
        update.message.reply_text(INTRO_TXT, parse_mode="Markdown", reply_markup=reply_markup)
    

    def search(self, title=None, author=None):
        try:
            if author != None and title == None:
                return self.library.search_author(author)
            elif author == None and title != None:
                return self.library.search_title(title)
            else:
                return []

        except Exception as e:
            self.logger.error("SearchError: "+str(e))

    def result_set(self, update, context, book_list):
        response = []
        for book in book_list:
            details = {}
            details["title"] = book['Title']
            details["author"] = book['Author']
            details["pub"] = book['Publisher']
            
            details["lang"] = book['Language']
            details["year"] = book['Year']

            details["page"] = book['Pages']
            details["type"] = book['Extension'].upper()
            details["size"] = book['Size']

            response.append(tg.InlineQueryResultArticle(id=book['ID'], description="{} | {} | {} | {}".format(details["author"], details["lang"], details["year"], details["type"]),
                input_message_content=tg.InputTextMessageContent(message_text=ABOUT_BOOK.format(*details.values()), parse_mode="Markdown"), title=details["title"],
                reply_markup=tg.InlineKeyboardMarkup([[tg.InlineKeyboardButton("Download ⏬", callback_data=book['Mirror_1'])]])))

        return response

    def callback_query(self, update, context):
        query = update.callback_query
        if '://' in query.data:
            download_links = self.library.resolve_download_links({'Mirror_1': query.data})
            context.bot.answerCallbackQuery(callback_query_id=update.callback_query.id, text="Downloading...Please wait", show_alert=False)
            
            if list(download_links.values())[0][-3:] == 'pdf':
                for value in download_links.values():
                    dwd_fail_flag = 0
                    try:
                        reply_markup = tg.InlineKeyboardMarkup(self.main_menu)
                        context.bot.send_document(chat_id=query.from_user.id, document=value, caption="Here's your file. Happy Reading. ☺", reply_markup=reply_markup)
                        dwd_fail_flag = 0
                        break
                    except Exception as e:
                        self.logger.error("DownloadError : "+str(e))
                        dwd_fail_flag = 1
                        continue
                    
                if dwd_fail_flag:
                    context.bot.send_message(chat_id=query.from_user.id, text="*Umm... Something went wrong.* 😕\n\nCould not download the file. Please try again with another file. :(", reply_markup=reply_markup)
            else:
                reply_markup = tg.InlineKeyboardMarkup([
                    [tg.InlineKeyboardButton('Direct Download', url=download_links['GET']), tg.InlineKeyboardButton('Cloudflare', url=download_links['Cloudflare'])],
                    [tg.InlineKeyboardButton('IPFS.io', url=download_links['IPFS.io']), tg.InlineKeyboardButton('Infura', url=download_links['Infura'])],
                    [tg.InlineKeyboardButton('◀ Back to Main Menu ', callback_data='redirect')]
                ])
                context.bot.send_message(chat_id=query.from_user.id, text="*Apologies... *😔\n\nTelegram does not support *auto-downloading* of a *non-pdf* document, yet. Please visit any of the links attached below to download the document.", parse_mode="Markdown", reply_markup=reply_markup)

        if query.data == 'redirect':
            reply_markup = tg.InlineKeyboardMarkup(self.main_menu)
            context.bot.send_message(chat_id=query.from_user.id, text="Have another go?", reply_markup=reply_markup)

        if query.data == 'cancel':
            context.bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
            context.bot.send_message(chat_id=query.message.chat.id, text="Sure, I wasn't doing anything anyway. ¯\_ಠಿ‿ಠ_/¯")

    def inline_query(self, update, context):
        query = update.inline_query.query

        if 'title' in query:
            articles = self.result_set(update, context, self.search(title=query.replace('title ', '')))
            try:
                update.inline_query.answer(results=articles, auto_pagination=True)
            except Exception as e:
                self.logger.error("InlineError: "+str(e))
        if 'author' in query:
            articles = self.result_set(update, context, self.search(author=query.replace('author ', '')))
            try:
                update.inline_query.answer(results=articles, auto_pagination=True)
            except Exception as e:
                self.logger.error("InlineError: "+str(e))


    def help(self, update, context):
        update.message.reply_text(HELP_TXT, parse_mode="Markdown", disable_web_page_preview=True)

    def dev(self, update, context):
        update.message.reply_text(DEV_TXT, parse_mode="Markdown")

    def error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)
        # text = "Hmmm. Something went wrong. \n\nThis wasn't supposed to happen though. Please try something else while we look into it. ʘ‿ʘ"
        # context.bot.send_message(chat_id=update.callback_query.from_user.id, text=text)
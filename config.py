import os
# ----------------------------------------------------------------------------------

PORT = os.environ.get('PORT', 5000)
URL = 'https://genesys-bot.herokuapp.com/'
TOKEN = os.environ.get('BOT_TOKEN')

# ----------------------------------------------------------------------------------

INTRO_TXT = """
Hi! I am *Genesis*, a digital librarian.

Search a book by title in here or use the commands and inline queries in private chats/groups for best results.
GLHF
"""

HELP_TXT = """
Need some help? I've got you covered.

*Available Functionalities*
Search by title "[@genesis_lib_bot](https://t.me/genesis_lib_bot) title <book name>"
Search by author "[@genesis_lib_bot](https://t.me/genesis_lib_bot) author <author name>"

*Tip*
Inline queries can be used in any private chat or group chat.
Have a nice day.
"""

DEV_TXT = """
Made with focus, commitment and sheer will and some py3 ;)
For any queries contact, [a_ignorant_mortal](https://t.me/a_ignorant_mortal)

More about the dev:
"""

DWD_ERROR = "*Umm... Something went wrong.* 😕\n\nCould not download the file. Please try again with another file. :("

DWD_EXCEPTION = "*Apologies... *😔\n\nTelegram does not support *auto-downloading* of a *non-pdf* document, yet. Please visit any of the links attached below to download the document."

# ----------------------------------------------------------------------------------

ABOUT_BOOK = """
*Title* - {}
*Author* - {}
*Publisher* - {}

*Language Published* - {}
*Year Published* - {}

*Pages* - {}
*File Type* - {}
*File Size* - {}
"""
.. Genesis Bot documentation master file, created by
   sphinx-quickstart on Sat Jul 17 10:42:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Genesis - A Telegram Bot
========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**INTRODUCTION**
================

Genesis, is a digital librarian (kinda). It operates off of Telegram.
It is connected internally to the legendary digital library **"The Library Genesis"**. 
With this project, I aimed at making the process of downloading any book/article from The Library Genesis
so easy that even a kid can do it.

Since, the website provides you with mirror links for any book/article you search, downloading
isn't actually "easy" per say. With this bot, you could just search for any document that might
be available publicly and it handles the ```downloading``` part for you and sends you the document
right in the chat.

**WORKING**
===========

Genesis, is an inline bot. For those who aren not that well versed with Telegram Bots, 
an inline bot can be summoned from any chat just (group or private) by mentioning it's name in the text field.

You can then mention ```title``` or ```author``` to search for documents with either its title 
or its author. After searching for the document in its vast database, you will be prompted with 
top 25 matching results for the query. 

Clicking on any of the result and then on the ```Download``` button will download the document and send it to you.

AS SIMPLE AS THAT.

.. figure:: _static/images/start.jpg
   :align: center
   
   Starting the bot.

.. figure:: _static/images/result.jpg
   :align: center
   
   Response from the bot after selecting a document from the list.

**LIMITATIONS**
===============

Well, like everything in this world. This too comes with a catch. 
Apparently, Telegram only allows bots to send documents to its clients which are PDFs. [```-_-```]

So in order to still serve the request, I built a work around to that. If you select a document from 
the results which is not a PDF document, the bot will still resolve the result but instead of 
directly sending out the document via Telegram chat (which is not allowed), it will send the links of 
the servers on which the document is hosted. The user can click on any of the links and the document 
will automatically be downloaded onto their devices.

.. figure:: _static/images/limit.jpg
   :align: center
   
   Response from the bot if the selected document isn't PDF.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from dateutil.relativedelta import relativedelta
import datetime

def calcular_tiempo(update, context):

    today = datetime.date.today()
    rd = relativedelta(datetime.date(2020,5,31),today)

    update.message.reply_text(
        'Quedan %(months)d meses y %(days)d dias, ha sido un placer amigos' % rd.__dict__ )

    return true

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1019768677:AAEWtgK_Sg7mMKjGn3jQVudKEmMuVhjbYN8", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    handler = MessageHandler(Filters.regex('IBM'), calcular_tiempo)

    dp.add_handler(handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          CallbackContext)
from dateutil.relativedelta import relativedelta
import datetime

from datetime import timedelta
from threading import Timer
import threading
import time

class Threading(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            t = datetime.datetime.today()
            future = datetime.datetime(t.year,t.month,t.day,10,00,00)
            time.sleep((future-t).seconds)
            time_left_schedule()
            time.sleep(5)

def time_left_schedule():
    bot = Bot("1019768677:AAEWtgK_Sg7mMKjGn3jQVudKEmMuVhjbYN8")
    today = datetime.datetime.today()
    rd = relativedelta(datetime.datetime(2020,5,31,10,00,00),today)

    bot.sendMessage("-326329345","Quedan %(months)d meses, %(days)d dias, %(hours)d horas, %(minutes)d minutos y %(seconds)d segundos para que IBM se haga con el poder, ha sido un placer amigos" % rd.__dict__ )

def time_left_reply(update, context):

    today = datetime.datetime.today()
    rd = relativedelta(datetime.datetime(2020,5,31,10,00,00),today)

    update.message.reply_text(
        'Quedan %(months)d meses, %(days)d dias, %(hours)d horas, %(minutes)d minutos y %(seconds)d segundos para que IBM se haga con el poder, ha sido un placer amigos' % rd.__dict__ )

def main():

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1019768677:AAEWtgK_Sg7mMKjGn3jQVudKEmMuVhjbYN8", use_context=True)
    tr = Threading()

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.regex('IBM'), time_left_reply))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
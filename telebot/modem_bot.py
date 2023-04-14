"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
#%% 
import logging
import os
import subprocess

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import modem_config as mc   #modem config obj
import modem_searchXL as ms #modem xl file search obj
import test as t
# Enable logging    
logging.basicConfig(
    filename='logtest.txt',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    
    user_says = " ".join(context.args)
    update.message.reply_text("""
    This bot is used to configure modem 
    /conf password number 
    or 
    /checkPing host 
    or
    /test url 
    
    """,user_says)
   
    
def checkPing(update,context): 
    #%%
    hostname = context.args[0]
    print(hostname)
    # cmd = "ping -c 4 " + hostname + " | grep '4 received' "
    cmd = "ping -c 4 " + hostname + " | grep '4 received' "
    
    print(cmd)
    p1 = subprocess.run([cmd], capture_output=True,text=True,shell=True)
    if p1.stdout:
        print(p1.stdout)
        x=p1.stdout 
    else : 
        print(p1.stdout)
        x=p1.stdout + "Host not found"
    update.message.reply_text("Ping Status " + hostname + " : " + x)

def test(update,context):
    text = t.testWeb()
    print(text)
    update.message.reply_text("Tested Given URL : " + text)


def conf(update,context):
    landline = context.args[0]

    mpass = context.args[1] 
    # username = context.args[2]
    # password = context.args[3]
    print(f"number - {landline} modem password - {mpass}")
    un,pwd = ms.searchUP(landline)
    print(f"username - {un} password - {pwd}")
    
    mc.configure(mpass,un,pwd)
    print(checkPing(update,context))

    update.message.reply_text("configured")


def stop(update,context):
    """Send a msg when command /stop is issued."""
    update.message.reply_text('Bot Stopped!')
  

# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # bot_token = os.environ.get('Telegram_Bot')
    bot_token='' #token here
    updater = Updater(bot_token)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("conf",conf))
    dispatcher.add_handler(CommandHandler("checkPing",checkPing))

    dispatcher.add_handler(CommandHandler("test", test))    #test 
    # on noncommand i.e message - echo the message on Telegram
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
   
    updater.idle()
    
    

if __name__ == '__main__':
    main()
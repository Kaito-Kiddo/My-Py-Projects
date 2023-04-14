# ! MY first bot 
#%%

#   user defined modules
import send_email as se
import nic_cred as nc
import ipabuse as ipa

# Inbuild Modules
from selenium import webdriver
import ipaddress as ip
import subprocess
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

bot_token =''    #Token here
bot = telegram.Bot(token= '1427569532:AAEpeXzVCHsfh39Yy3A12BKYvm1I55LVM7E')

driver_path = "C:/Users/kaito/Work Code/Telegram Python Bots/chromedriver.exe"
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help or /start is issued."""
    
    user_says = " ".join(context.args)
    fs = f"""
    This bot has following commands 
    /start args
    gives info about bot and appends with whatever user types 
    
    /searchxl   phone_number
    searches an excel file and returns username & password for the given MTNL landline number

    
    /mail receiver_email_addr
    sends a demoxl.xlsx file to the receipient 
    If none receiver provided then it will send mail to default receiver!

    /browse elemnt_to_find
    finds given element class name in given host  
    and returns class for that elt in telegram chat
    
    /ping hostname
    returns host online or offline
    
    /stop  
    stops the bot
    """ + user_says
    update.message.reply_text(fs)

def ipabuse(update,context):
    ip_addr= ip.ip_address(context.args[0])
    if ip_addr.is_global : 
        ip_dict = ipa.abuse(str(ip_addr))   # abuse function accepts a string value and ip_addr is ipaddress object
        output = ""
        for key,value in ip_dict.items():
            output += f"{key} : {value}\n"
        update.message.reply_text(output)
    else : 
        fs = f"{ip_addr} is not global IPv4 Addr"
        update.message.reply_text(fs)


def search_xl(update,context):
    pno = context.args[0]
    credentials = nc.searchUP(pno)
    fs = f"Username : {credentials[0]} \nPassword : {credentials[1]} \n" 
    update.message.reply_text(fs)
    

def browse(update: Update, context: CallbackContext) :
    
    
    if (len(context.args) != 2):
        elt_to_find = "container"
        hostname = "inventwithpython.com"
        fs = f"Checking {elt_to_find} in {hostname}"
        update.message.reply_text(fs)
    else:
        elt_to_find =context.args[0]
        hostname = context.args[1]
        fs = f"Checking {elt_to_find} in {hostname}"
        update.message.reply_text(fs)
    # option.add_argument("--incognito") OPTIONAL
    # option.add_argument("--headless") OPTIONAL

    # Create new Instance of Chrome
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    browser.get("https://www."+hostname)

    try:
        elem = browser.find_element_by_class_name(elt_to_find)
        fs1 = f'Found <{elem.tag_name}> element with that class name {elem}!'
        print(fs1)
        update.message.reply_text(fs1)
    except:
        fs2 = f'Was not able to find an element with that name.'
        update.message.reply_text(fs2)

def start(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    
    user_says = " ".join(context.args)
    reply = "Press /help for BOT INFO " + user_says
    
    update.message.reply_text(reply.upper())


def stop(update,context):
    """Send a msg when command /stop is issued."""
    update.message.reply_text('Bot Stopped!')


def checkPing(update,context): 
    hostname = context.args[0]
    print(hostname)
    # cmd = "ping -c 4 " + hostname + " | grep '4 received' "

    p = subprocess.Popen(f'ping {hostname}')
    p.wait()    
    print(type(p))
    print(str(p))
    if p.poll() == 0:
        x="online"
        print("Online")
    else : x="offline"
    update.message.reply_text("Ping Status " + hostname + " : " + x)

def mail(update,context):
    if (len(context.args) == 2):
        Msub= context.args[0]
        Mto=context.args[1]
        se.mail(Msub,Mto)
    else:
        se.mail()

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # bot_token = os.environ.get('Telegram_Bot')
    updater = Updater(bot_token)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", help))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler('browse', browse))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('ping',checkPing))
    dispatcher.add_handler(CommandHandler('mail',mail))
    dispatcher.add_handler(CommandHandler("searchxl", search_xl))
    dispatcher.add_handler(CommandHandler("ipabuse",ipabuse))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
   
    updater.idle()
    
    

if __name__ == '__main__':
    main()

# %%

import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from telegram.message import Message
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def sendMessage(text: str, bot, update: Update):
        return bot.send_message(update.message.chat_id,
                                reply_to_message_id=update.message.message_id,
                                text=text, parse_mode='HTMl',
                                disable_web_page_preview=True)
 
        
def deleteMessage(bot, message: Message):
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)
        
def bypass(update, context):
        if len(context.args) == 0: #If no url is sent, than this will show this msg
            logging.info("Error: No Link provided!")
            update.message.reply_text(f"**No Link Detected**\nUSAGE: /url yourlink.. ") 
        else:
            url = context.args[0]
            res = get_tld(url, as_object=True)
            logging.info(f"Link detected: {url}")

        if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
                if (res.domain == "link-center"):
                        msg = sendMessage(f"Processing: [Your-Link]({url})", context.bot, update)
                        logging.info(f"Processing: {url}")
                        bypassed_link = bypasser.bypass(url, name="linkvertise")
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"**Link Bypassed Successfully**\nn`{bypassed_link}`",                        
                                        parse_mode="Markdown",
                                        disable_web_page_preview=True,
                                        quote=True)

                else:
                        msg = sendMessage(f"Processing: {url}", context.bot, update)
                        logging.info(f"Processing: {url}")
                        bypassed_link = bypasser.bypass(url)
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"**Ad Link Bypassed!**\n\n{bypassed_link}",                            
                                        parse_mode="Markdown",
                                        disable_web_page_preview=True,
                                        quote=True)
                logging.info("Link bypassed successfully!")
        else:

                update.message.reply_text(f"{res.domain} domain links not supported till now", 
                                    parse_mode="Markdown",
                                    disable_web_page_preview=True,
                                    quote=True)
                logging.info("Error: Link not supported!")

   
def start(update: Update, context: CallbackContext):
    update.message.reply_photo(photo="https://te.legra.ph/file/404503e13fac593ada12d.jpg", caption="Hey Am Kid and I have Something 😉😜\n\nHo Gaya Ab Send Kr Link ") 
    logging.info("/start")


    
def unknown_text(update: Update, context: CallbackContext):
        update.message.reply_text(
            f"Sorry I can't recognize you , you said '{update.message.text}'")
        logging.info("unknown command!")
  
def unknown(update: Update, context: CallbackContext):
        update.message.reply_text(
            f"Sorry '{update.message.text}' is not a valid command")    

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')
 
def main():
    
    TOKEN = '6284968138:AAEeFoLmmQS-MeIvkeAcnNpx-aEveLvIp2w'
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    updater.dispatcher.add_handler(CommandHandler('url', bypass))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
    updater.dispatcher.add_error_handler(error)
  
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'https://smexxx.herokuapp.com' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()

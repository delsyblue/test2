#lib
import socket 
import telebot
import socks
from pynput.keyboard import  Listener
#........................................................#
def add():
    input("your massage : ")
#........................................................#
Token = "1723680974:AAHhkO58zrvcH8ofZxST289701bMSQMk2js"
Bot = telebot.TeleBot(Token)
#........................................................#
@Bot.message_handler(content_types=['text'])


def botmain(user):
    
    username = user.chat.username
    name = user.chat.first_name
    chatid = user.chat.id
    txt = user.text
    msg = user.message_id

      
    print("""***************************************************
{}
          @{}
          {}
          {}""".format(name , username , chatid , txt))

    if chatid == 638340455:
        Bot.send_message(1758844141,txt)

    else:
        Bot.forward_message(638340455 , chatid, msg)

#........................................................#
Bot.polling(True)

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import re

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'/input(вводите внутри одного сообщения "/input имя фамилия телефон комментарий")\n/found(вводите внутри одного сообщения "/found фамилия")\n/sort\n/output\n')

def import_names(update: Update, context: CallbackContext) -> None:
    log(update, context)
    try:
        log(update, context)
        num = update.message.text
        num = num.split()
        num = ", ".join(num[1:])
        rec=open("telephones.txt", "a", encoding="UTF-8")
        rec.write("\n"+num)
        update.message.reply_text('Информация записана в справочник')
        rec.close()

    except:
        update.message.reply_text("Ошибка ввода")

def export(update: Update, context: CallbackContext) -> None:
    log(update, context)
    try:
        log(update, context)
        num = update.message.text
        num = num.split()
        search_line=", ".join(num[1:3])
        r=open("telephones.txt", "r", encoding="UTF-8")
        x=r.readlines()
        for i in x:
            if search_line in i:
                opt=re.sub(r"[,]\s"," ", str(i))
                update.message.reply_text(opt)
        r.close()

    except:
        update.message.reply_text("Ошибка ввода")

def sort_file(update: Update, context: CallbackContext) -> None:
    x=open("telephones.txt", "r", encoding="UTF-8")
    my_list=[(line.strip()) for line in x.readlines() if len(line.strip())]
    my_list=sorted(my_list,key=lambda i:(((i.split(","))[0])))
    x.close()
    x=open("telephones.txt", "w", encoding="UTF-8")
    for i in my_list:
        x.write(i+"\n")
    x.close()


def output(update: Update, context: CallbackContext) -> None:
    x=open("telephones.txt", "r", encoding="UTF-8")
    a=x.read()
    opt=re.sub(r"[,]\s"," ", str(a))
    update.message.reply_text(opt)
    x.close()



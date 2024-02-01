from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import datetime
import requests
from bs4 import BeautifulSoup

listName = []
listDes = []
listHref = []


def parser():

    global listName
    global listDes
    global listHref

    url = "https://uaserials.pro/films/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    for a in soup.find_all('a', href=True):
        u = a['href']
        if u.startswith("http"):
            listHref.append(u)
            requst = requests.get(u)
            soup1 = BeautifulSoup(requst.text, features="html.parser")
            soup_list_name = soup1.find_all('span', {'class': 'oname_ua'})
            if len(soup_list_name) > 0:
                listName.append(soup_list_name[0].text)
            soup_list_ul = soup1.find_all('ul', {'class': 'short-list fx-1'})
            for i in soup_list_ul:
                listDes.append(i.text)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.datetime.now()
    await update.message.reply_text(f'{now}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parser()
    for film in range(len(listName)):
        await update.message.reply_text(f'{listName[film]} \n{listDes[film]} \n{listHref[film]}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/now\n/film')



app = ApplicationBuilder().token("6701915790:AAFENFj5LM21HEFe9TYgq3cA6-A0_faT75g").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("now", now))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", help))

app.run_polling()
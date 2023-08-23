# Copyright 2021 TerminalWarlord under the terms of the MIT
# license found at https://github.com/TerminalWarlord/TikTok-Downloader-Bot/blob/master/LICENSE
# Encoding = 'utf-8'
# Fork and Deploy, do not modify this repo and claim it yours
# For collaboration mail me at dev.jaybee@gmail.com
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
import shutil
import requests
import json
import os
import re
from bs4 import BeautifulSoup as bs
import time
from datetime import timedelta
import math
import base64
from progress_bar import progress, TimeFormatter, humanbytes
from dotenv import load_dotenv

#load_dotenv()
bot_token = '5879955645:AAE1bRY-aDbbLN9MFReTwvLlrLnO3v5ZwvA'
workers = 4
api = 12435439
hash = '8fba0f88315f829b034f79c5cbd2c3d4'
chnnl = 'https://t.me/testingsessuin'
BOT_URL = 'tk_ig_downloader_bot'
app = Client("JayBee", bot_token=bot_token, api_id=api, api_hash=hash, workers=workers)



@app.on_message(filters.command('start'))
def start(client, message):
    kb = [[InlineKeyboardButton('Channel 🛡', url=chnnl),InlineKeyboardButton('Repo 🔰', url="https://github.com/gaurang-py/")]]
    reply_markup = InlineKeyboardMarkup(kb)
    app.send_message(chat_id=message.from_user.id, text=f"📱  Hey Mate 📱  /n👉   I am **TikTok/Instagram Downloader Bot**.\n I can download TikTok video or Instagram Post/Reels/Stories without Watermark.\n\n"
                          "[📌] Developer : GAURANG \n"
                          "[📌] Language : Python \n"
                          "[📌] Framework : 🔥 Pyrogram ",
                     parse_mode='md',
                     reply_markup=reply_markup)


@app.on_message(filters.command('help'))
def help(client, message):
    kb = [[InlineKeyboardButton('Channel 🛡', url=chnnl),InlineKeyboardButton('Repo 🔰', url="https://github.com/gaurang-py/")]]
    reply_markup = InlineKeyboardMarkup(kb)
    app.send_message(chat_id=message.from_user.id, text=f"📱  Hey Mate 📱  /n👉   I am **TikTok/Instagram Downloader Bot**.\n I can download TikTok video or Instagram Post/Reels/Stories without Watermark.\n\n"
                          "[📌] Developer : GAURANG \n"
                          "[📌] Language : Python \n"
                          "[📌] Framework : 🔥 Pyrogram ",
                     parse_mode='md',
                     reply_markup=reply_markup)



@app.on_message((filters.regex("http://")|filters.regex("https://")) & (filters.regex('tiktok')|filters.regex('douyin')))
def tiktok_dl(client, message):
    a = app.send_message(chat_id=message.chat.id,
                         text=' ⏳ Downloading File to the Server ⏳ ',
                         parse_mode='md')
    link = re.findall(r'\bhttps?://.*[(tiktok|douyin)]\S+', message.text)[0]
    #print(link)
    link = link.split("?")[0]
    #print(link)
    params = {
      "link": link
    }
    headers = {
      'x-rapidapi-host': "tiktok-info.p.rapidapi.com",
      'x-rapidapi-key': "19baab40eamshe27bd6d38d664f8p182b65jsn06dfa40cc274"
    }
    
    ### Get your TikTok API from https://rapidapi.com/TerminalWarlord/api/tiktok-info/
 
    api = f"https://tiktok-info.p.rapidapi.com/dl/"
    r = requests.get(api, params=params, headers=headers).json()['videoLinks']['download']
    directory = str(round(time.time()))
    filename = str(int(time.time()))+'.mp4'
    size = int(requests.head(r).headers['Content-length'])
    total_size = "{:.2f}".format(int(size) / 1048576)
    try:
        os.mkdir(directory)
    except:
        pass
    with requests.get(r, timeout=(50, 10000), stream=True) as r:
        r.raise_for_status()
        with open(f'./{directory}/{filename}', 'wb') as f:
            chunk_size = 1048576
            dl = 0
            show = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                dl = dl + chunk_size
                percent = round(dl * 100 / size)
                if percent > 100:
                    percent = 100
                if show == 1:
                    try:
                        a.edit(f'🔗 URL : {message.text} \n'
                               f'⏱ Total Size : {total_size} MB\n'
                               f'⏱ Downloaded : {percent}%\n',
                               disable_web_preview=False)
                    except:
                        pass
                    if percent == 100:
                        show = 0

        a.edit(f'⏳ Downloaded to the server! ⏳\n'
               f'⏳ Uploading to Telegram Now ⏳')
        start = time.time()
        title = filename
        app.send_document(chat_id=message.chat.id,
                          document=f"./{directory}/{filename}",
                          caption=f"📁 File :📁 {filename}\n"
                          f"🔗 Size : 🔗 {total_size} MB\n\n"
                          f" Uploaded by @{BOT_URL}__",
                          file_name=f"{directory}",
                          parse_mode='md',
                          progress=progress,
                          progress_args=(a, start, title))
        a.delete()
        try:
            shutil.rmtree(directory)
        except:
            pass


@app.on_message((filters.regex("http://")|filters.regex("https://")) & (filters.regex('instagram')|filters.regex('douyin')))
def insta_dl(client, message):
    try:
        a = app.send_message(chat_id=message.chat.id,
                                text='__Downloading File to the Server__',
                                parse_mode='md')
        link = re.findall(r'\bhttps?://.*[(instagram|douyin)]\S+', message.text)[0]
        #print(link)
        link = link.split("?")[0]
        url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

        querystring = {"url":"https://instagram.com/stories/paruluniversity/3039321956263830072?utm_source=ig_story_item_share&igshid=YmMyMTA2M2Y="}

        headers = {
        "X-RapidAPI-Key": "19baab40eamshe27bd6d38d664f8p182b65jsn06dfa40cc274",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.json())
        try:
            typ = response.json()['Type']
        except:
            pass
        if 'Video' in typ:
            print("Video")
            dm= response.json()['media']
            #dm = 'https://scontent.cdninstagram.com/v/t50.2886-16/330132608_555903459848335_7956301309536568292_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=107&_nc_ohc=0b054FDy2vkAX_WV4UZ&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAOo6-G4cX82678mLstA9dKbYQYkzz6PQHiLFBAzGKj-A&oe=63F0727C&_nc_sid=978cb9&dl=1&'

            directory = str(round(time.time()))
            filename = str(int(time.time()))+'.mp4'
            size = int(requests.head(dm).headers['Content-length'])
            total_size = "{:.2f}".format(int(size) / 1048576)

            r = requests.get(dm, allow_redirects=True)
            try:
                os.mkdir(directory)
            except:
                pass
            open(f'./{directory}/{filename}', 'wb').write(r.content)
            print(size)
            print(total_size)
            a.edit(f'__Downloaded to the server!\n'
                        f'Uploading to Telegram Now ⏳__')
            start = time.time()
            title = filename
            app.send_document(chat_id=message.chat.id,
                                document=f"./{directory}/{filename}",
                                caption=f"**File :** __{filename}__\n"
                                f"**Size :** __{total_size} MB__\n\n"
                                f"__Uploaded by @{BOT_URL}__",
                                file_name=f"{directory}",
                                parse_mode='md',
                                progress=progress,
                                progress_args=(a, start, title))
            a.delete()
            try:
                shutil.rmtree(directory)
            except:
                pass
        elif 'Post-Image' in typ:
            print('image')
            #dm = 'https://scontent.cdninstagram.com/v/t50.2886-16/330132608_555903459848335_7956301309536568292_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=107&_nc_ohc=0b054FDy2vkAX_WV4UZ&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAOo6-G4cX82678mLstA9dKbYQYkzz6PQHiLFBAzGKj-A&oe=63F0727C&_nc_sid=978cb9&dl=1&'
            dm= response.json()['media']
            directory = str(round(time.time()))
            filename = str(int(time.time()))+'.jpeg'
            size = int(requests.head(dm).headers['Content-length'])
            total_size = "{:.2f}".format(int(size) / 1048576)

            r = requests.get(dm, allow_redirects=True)
            try:
                os.mkdir(directory)
            except:
                pass
            open(f'./{directory}/{filename}', 'wb').write(r.content)
            print(size)
            print(total_size)
            a.edit(f'__Downloaded to the server!\n'
                        f'Uploading to Telegram Now ⏳__')
            start = time.time()
            title = filename
            app.send_document(chat_id=message.chat.id,
                                document=f"./{directory}/{filename}",
                                caption=f"**File :** __{filename}__\n"
                                f"**Size :** __{total_size} MB__\n\n"
                                f"__Uploaded by @{BOT_URL}__",
                                file_name=f"{directory}",
                                parse_mode='md',
                                progress=progress,
                                progress_args=(a, start, title))
            a.delete()
            try:
                shutil.rmtree(directory)
            except:
                pass
    except:
        pass

app.run()

import urllib.request as req
import bs4
from datetime import datetime
from operator import itemgetter
import re
import os
import subprocess
import yt_dlp
def download(url):
    num = 0
    with open("cnt.txt", "r") as cnt:
        num = int(cnt.read())
    command = [
        'yt-dlp',
        '--output', os.path.join("mp3", f'{num}'),
        '--embed-thumbnail',
        '--add-metadata',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '320K',
        url
    ]
    
    try:
        subprocess.run(command, check=True)
        print('音訊已成功下載並轉換為 MP3 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')
        
    command = ['yt-dlp', '--write-thumbnail', '--convert-thumbnails', 'jpg', '--skip-download',  '--output', os.path.join("img", f'{num}') ,url]
    try:
        subprocess.run(command, check=True)
        print('圖片已成功下載並轉換為 jpg 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')
    num += 1
    with open("cnt.txt", "w") as cnt:
        cnt.write(f'{num}')
    return (num - 1)

def get_video_title(video_url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict.get('title', None)
        
def save_to_html(title, num, filename="yuiko.html"):
    head_content = ""
    tail_content = ""
    body_content = ""
    html_content = ""
    upd_body = ""
    with open("head.html", "r") as head:
        head_content = head.read()
    with open("body.html", "r") as body:
        body_content = body.read()
    with open("../tail.html", "r") as tail:
        tail_content = tail.read()
    html_content += head_content
    upd_body += body_content
    upd_body += f"{{ src: 'mp3/{num}.mp3', name: '{title}', artist: 'yuiko', img: 'img/{num}.jpg' }},\n"
   
    html_content += upd_body
    html_content += tail_content
    with open(filename, "w") as file:
        file.write(html_content)
    with open("body.html", "w") as body:
        body.write(upd_body)

url = input("請輸入影片網址： ")
num = download(url)
title = get_video_title(url)
save_to_html(title, num)

import os
import subprocess

def download_mp4(url, num):
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
        print('音訊已成功下載並轉換為 MP4 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')
        
    command = ['yt-dlp', '--write-thumbnail', '--convert-thumbnails', 'jpg', '--skip-download',  '--output', os.path.join("img", f'{num}') ,url]
    try:
        subprocess.run(command, check=True)
        print('圖片已成功下載並轉換為 jpg 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')

youtube_url = input("請輸入YouTube視頻URL: ")
num = input("請輸入檔名（編號）: ")

download_mp4(youtube_url, num)


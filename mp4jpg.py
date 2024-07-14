import os
import subprocess

def download_mp4(url):
    #command = ['yt-dlp', '--output', os.path.join('%(title)s'), url]
    #command = ['yt-dlp', url]
    #command = ['yt-dlp', '--paths', output_dir, '-o', file_name, url]
    
    command = [
        'yt-dlp',
        '-f', 'mp4',
        url
    ]
    
    try:
        subprocess.run(command, check=True)
        print('音訊已成功下載並轉換為 MP4 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')
        
    command = ['yt-dlp', '--write-thumbnail', '--convert-thumbnails', 'jpg', '--skip-download', url]
    try:
        subprocess.run(command, check=True)
        print('圖片已成功下載並轉換為 jpg 格式')
    except subprocess.CalledProcessError as e:
        print(f'下載或轉換過程中發生錯誤：{e}')

youtube_url = input("請輸入YouTube視頻URL: ")

download_mp4(youtube_url)


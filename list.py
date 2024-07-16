import yt_dlp
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設置你的 YouTube Data API v3 金鑰
API_KEY = 'AIzaSyBMlNYdMc2ZxY-Ccv38n4QZ0_b6NT-i5LI'

def get_playlist_videos(playlist_url):
    ydl_opts = {
        'quiet': True,  # 不顯示詳細日誌
        'extract_flat': True,  # 只需提取影片資訊，不需下載
        'youtube_api_key': API_KEY,  # 設置 YouTube Data API v3 金鑰
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        if 'entries' in result:
            # 如果是播放清單，取得所有影片的連結
            video_links = []
            for entry in result['entries']:
                video_id = entry['id']
                video_link = f'https://www.youtube.com/watch?v={video_id}'
                video_links.append(video_link)
            return video_links
        else:
            # 如果不是播放清單，直接返回影片連結
            video_id = result['id']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            return [video_link]

# 測試程式碼
playlist_url = 'https://youtube.com/playlist?list=PL1lvmDJ8mJgGxYYF_ptXBWIIxCeymri4w&si=1-A_WaogRCvVtuSt'  # 替換為你的播放清單 URL
try:
    video_links = get_playlist_videos(playlist_url)
    num = 1
    for link in video_links:
        print(num, link)
        num += 1
except HttpError as e:
    print(f'HttpError occurred: {e}')
except yt_dlp.utils.DownloadError as e:
    print(f'DownloadError occurred: {e}')


import os
import yt_dlp

url = input("保存したいYouTubeのURLを入力してください: ")
mp = input("ファイルの種類を入力してください(mp3 or mp4): ")
path = int(input("ダウンロードフォルダに保存したい場合は1、\nyoutube.py がある所に保存したい場合は2を入力してください: "))

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
if mp == "mp4":
 if path == 1:
  ydl_opts = {
     'format': 'bestvideo+bestaudio',
     'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
     'merge_output_format': 'mp4',
  }
 if path == 2:
   ydl_opts = {
     'format': 'bestvideo+bestaudio',
     'outtmpl': 'youtubevideo/%(title)s.%(ext)s',
     'merge_output_format': 'mp4',
  }

if mp == "mp3":
    if path == 1:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  
            }],
        }
    if path == 2:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'youtubevideo/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

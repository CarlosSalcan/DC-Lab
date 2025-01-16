import yt_dlp as yt_dlp

def download_YT(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) 

url = "https://www.youtube.com/watch?v=t2DVBosz9Xs"
download_YT(url)

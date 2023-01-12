from pytube import YouTube
from pytube.cli import on_progress

link = "https://www.youtube.com/watch?v=aJaBpfodRI4"
SAVE_PATH = ""  

def Download(link):
    video = YouTube(link,on_progress_callback=on_progress)
    video.streams.first()
    video.streams.get_highest_resolution()
    try:
        video.download(SAVE_PATH, 'video','mp4'  
)
    except:
        print("An error has occurred")

Download(link)

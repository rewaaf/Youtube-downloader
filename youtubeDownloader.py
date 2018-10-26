# single video

from pytube import YouTube

link = input('Hello to YouTube Downloader\nPlease enter link of the video: ')
video = YouTube(link)
vname = video.title
print('The video title is: '+vname)
quality = video.streams.filter(mime_type="video/mp4").all()
print('Video quality: ')
for qua in quality:
    print(qua.resolution)
selection = input('Enter video quality such as (720p): ')
selectedvideo = video.streams.filter(res=selection).first()
selectedvideo.download('/put your path here')
print('Thank you for downloading!')

# playlist

from pytube import Playlist

link = input('Please enter the link of the playlist: ')
playlist = Playlist(link)
playlist.download_all('/put your path here')
print('Thank you for downloading!')

import tkinter
import youtube_dl

ydl_opts = {
    'nocheckcertificate': True,
    'outtmpl': '/Users/linaliu/Movies/youtube/game_of_throne'
} #
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/ptIPlGTuuJo?list=PLlW7FKuvkLmwNRNnlMY8WedlcKptZ7TfJ&t=2022'])

print('done')

#youtube-dl --all-subs --skip-download https://www.youtube.com/watch?v=Ye8mB6VsUHw
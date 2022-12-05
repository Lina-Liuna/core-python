import tkinter
import youtube_dl

ydl_opts = {
    'nocheckcertificate': True,
    'outtmpl': '/Users/linaliu/Movies/youtube/'
} #
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=iN8PKcNGcuI'])

print('done')

#youtube-dl --all-subs --skip-download https://www.youtube.com/watch?v=Ye8mB6VsUHw
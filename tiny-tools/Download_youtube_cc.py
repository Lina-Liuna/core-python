import youtube_dl
import os

ydl_opts = {
    'nocheckcertificate': True,
    'writesubtitles': True,
    'allsubtitles:': True,
    'writeautomaticsub': True,
    'skip_download': True,
    'listsubtitles': True,
    'subtitleslangs': ['en'],

}

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     # ydl.download(['https://www.youtube.com/watch?v=QfJsau0ItOY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg'])
#     ydl.download(['https://www.youtube.com/watch?v=AOqF5saQPx4'])
#
# print('done')
filedir = '/Users/linaliu/code/core-python/teeny_tiny_funny_tools/'
filename = 'test.srt'
from youtube_transcript_api import YouTubeTranscriptApi

#print(help(YouTubeTranscriptApi.get_transcript))
# the parameter is in url string after character v=
srt = YouTubeTranscriptApi.get_transcript("T53EyLPj4UM&list=PLot-Xpze53lcBX3BPCUoqlt4-KL-3XFHz&index=2")
with open(filedir + filename, 'w') as f:
    for item in srt:
        f.write(list(item.values())[0],)
        f.write('\n')

print(list(srt))



#youtube-dl --all-subs --skip-download https://www.youtube.com/watch?v=Ye8mB6VsUHw
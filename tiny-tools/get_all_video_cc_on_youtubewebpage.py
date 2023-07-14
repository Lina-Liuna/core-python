import requests
import re
import youtube_dl
import os
from youtube_transcript_api import YouTubeTranscriptApi



ydl_opts = {
    'nocheckcertificate': True,
    'writesubtitles': True,
    'allsubtitles:': True,
    'writeautomaticsub': True,
    'skip_download': True,
    'listsubtitles': True,
    'subtitleslangs': ['en'],

}
# Make an HTTP request to the website
youtubesite = "https://www.youtube.com/@abc7news/videos?view=0&sort=dd&shelf_id=0"  # Replace with the URL of the website you want to parse


def get_all_matches(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")  # Replace "utf-8" with the correct encoding if needed
    # Find the string starting with "/watch?v=" and ending with """
    matches = re.findall(r'"/watch\?v=([^"]+)"', content)

    # Print the matches
    for match in matches:
        print('https://www.youtube.com/watch?v=' + match)
    return matches

youtube_links = get_all_matches(youtubesite)


# the parameter is in url string after character v=
def get_cc(filename, urllink):
    srt = YouTubeTranscriptApi.get_transcript(urllink)
    with open(filename, 'w') as f:
        for item in srt:
            f.write(list(item.values())[0], )
            f.write('\n')

    print(list(srt))

def write_all_cc_to_file(urlinks):
    for linkstr in urlinks:
        get_cc('/Users/linaliu/code/core-python/tiny-tools/youtube_cc/ABC7_News_Bay_Area_today_cc/'+linkstr+'.txt', linkstr)


write_all_cc_to_file(youtube_links)


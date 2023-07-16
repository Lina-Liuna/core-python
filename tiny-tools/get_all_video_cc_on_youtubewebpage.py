import requests
import re
import youtube_dl
import os
from youtube_transcript_api import YouTubeTranscriptApi




# Make an HTTP request to the website
youtubesite = "https://www.youtube.com/@abc7news/videos"  # Replace with the URL of the website you want to parse


def get_all_matches(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")  # Replace "utf-8" with the correct encoding if needed
    # Find the string starting with "/watch?v=" and ending with """
    matches = re.findall(r'"/watch\?v=([^"]+)"', content)
    # Print the matches
    for match in matches:
        print('https://www.youtube.com/watch?v=' + match)
    titles = re.findall(r'"title":{"runs":\[\{"text":"(.*?)"\}\],', content)

    return (titles, matches)

(youtube_titles, youtube_links) = get_all_matches(youtubesite)


# the parameter is in url string after character v=
def get_cc(filename, urllink):
    srt = YouTubeTranscriptApi.get_transcript(urllink)


    with open(filename, 'w') as f:
        for item in srt:
            f.write(list(item.values())[0], )
            f.write('\n')

def write_all_cc_to_file(titles, urlinks):
    for title, linkstr in zip(titles, urlinks):
        print(title)
        get_cc('/Users/linaliu/code/Booklist/gallery/youtube/newstoday/'+ title +'.txt', linkstr)


write_all_cc_to_file(youtube_titles,youtube_links)


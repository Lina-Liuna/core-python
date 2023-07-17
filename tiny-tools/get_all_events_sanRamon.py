import requests
import re
import youtube_dl
import os
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import date

# Make an HTTP request to the website
youtubesite = "https://www.youtube.com/@cbssacramento/videos"  # Replace with the URL of the website you want to parse


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
    try:
        srt = YouTubeTranscriptApi.get_transcript(urllink)
    except Exception as e:
        print(f"Transcript retrieval failed: {e}")
        return


    filename = filename.replace('/', '_')
    with open(filename, 'w') as f:
        for item in srt:
            f.write(list(item.values())[0], )
            f.write('\n')

def write_all_cc_to_file(titles, urlinks):
    today = date.today()
    formatted_date = today.strftime("%d_%m_%Y")
    folder_path = '/Users/linaliu/code/Booklist/gallery/youtube/cbssacramento' + formatted_date  + '/'
    if not os.path.exists(folder_path):
        # Create the folder
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
    for title, linkstr in zip(titles, urlinks):
        print(title)

        get_cc(folder_path  + title +'.txt', linkstr)


write_all_cc_to_file(youtube_titles,youtube_links)


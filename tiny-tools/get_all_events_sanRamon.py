import requests
import re
import youtube_dl
import os
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import date

import requests
from bs4 import BeautifulSoup

# Make an HTTP request to the website
sanramonsite = "https://patch.com/california/sanramon/calendar"  # Replace with the URL of the website you want to parse


def get_all_matches(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")  # Replace "utf-8" with the correct encoding if needed
    print(content)





def get_website_content(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the divs using the specified class name
        divs_titles = soup.find_all('div', class_="styles_TextWrapper__20_40")

        # Extract the content of each div
        title_list = [div.get_text() for div in divs_titles]
        div_dates = soup.find_all('div', class_="calendar-icon__date")
        # Extract the content of each div
        date_list = [div.get_text() for div in div_dates]

       # Find all the <a> tags
        anchor_tags = soup.find_all('a')

        # Extract the href values from the <a> tags
        href_values = [tag['href'] for tag in anchor_tags if 'href' in tag.attrs]
        comapre_len = len('/california/sanramon/calendar/event/20230717/5cf1e0fd-19c0-4da5-b874-175c8fa86801/')
        href_values = list(set(href_values))
        href_values = [string for string in href_values if '/california/sanramon/calendar/event/' in string]

        href_values = sorted(href_values, key=lambda x: x.split("/")[5])
        filename = '/Users/linaliu/code/Booklist/gallery/sanramonevent.txt'
        with open(filename, 'w') as f:
            for href, title in zip(href_values, title_list):
                content_line = href.split("/")[5] + ':' + title + ':'
                f.write(content_line)
                f.write('\n\n')
                f.write('https://patch.com'+ href)
                f.write('\n\n')

            print()


    else:
        # Request was not successful
        print(f"Error: {response.status_code}")

# Provide the URL of the website you want to retrieve the content from
website_url = "https://patch.com/california/sanramon/calendar"

# Call the function to get the website content
get_website_content(website_url)




import requests
from bs4 import BeautifulSoup

import re

# Make an HTTP request to the website
url = "https://www.youtube.com/@abc7news/videos?view=0&sort=dd&shelf_id=0"  # Replace with the URL of the website you want to parse
response = requests.get(url)
content = response.content.decode("utf-8")  # Replace "utf-8" with the correct encoding if needed
# Find the string starting with "/watch?v=" and ending with """
matches = re.findall(r'"/watch\?v=([^"]+)"', content)

# Print the matches
for match in matches:
    print('https://www.youtube.com/watch?v=' + match)
import requests
from bs4 import BeautifulSoup

# Define the search query
query = "nephrotomy"

# Perform the search and retrieve the HTML content
url = f"https://www.google.com/search?q={query}"
response = requests.get(url)
html_content = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the search result elements and extract the URLs
search_results = soup.find_all("a")
for result in search_results:
    href = result.get('href')
    if href.startswith('/url?q='):
        url = href[len('/url?q='):]
        print(url)
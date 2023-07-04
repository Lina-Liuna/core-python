from googlesearch import search

# Define the search query
query = "nephrotomy"

# Perform the search and retrieve the results
search_results = search(query )  # You can specify the number of results you want

# Iterate over the search results and print them
for result in search_results:
    print(result)
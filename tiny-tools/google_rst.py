import googlesearch
# Define the search query
query = "nephrotomy"

# Create an instance of GoogleSearch
results = googlesearch.search(query)



# Iterate over the search results and print them
for result in results:
    print(result)
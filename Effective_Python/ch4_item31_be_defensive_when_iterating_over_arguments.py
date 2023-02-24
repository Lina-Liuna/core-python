# Example: I want to analyze tourism numbers for the U.S. state of Texas,
# the data set is the number of visitors to each city
# I'd like to figure out what percentage of overall tourism each city receives.

# I need a normalization function that sums the inputs to determine the total number of tourists per year
# and then divides each city's individual visitor count by the total to find that city's contribution to the whole.

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        yield  percent

visits = [56, 78, 95]
percentages = normalize(visits)
print(list(percentages))
print(sum(list(percentages), 0))


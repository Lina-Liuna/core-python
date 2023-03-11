import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())
air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)
print(air_quality.head())

# soring by one or more columns is supportted by sort_values
# with DataFrame.sort_values(), the rows in the table are sorted according to the defined columns
# the index follow the row order
print(titanic.sort_values(by='Age').head())
print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())

# filter the subset
no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)
# the pivot() function is purely reshaping/restructuring of the data: a single value for each index/column combination is required.
print(no2_subset.pivot(columns="location", values="value"))

no2.pivot(columns="location", values="value").plot()
plt.show()

# pivot() return data only rearranged, when multiple vlaue need to be aggregated, pivot_table() can be used.
# Providing an aggregation function on how to combine these values.

# pivot_table is well known concept in spreadsheet software
# pivot_table support aggregations.
print(air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
))

print(air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
))

# Add new index to the DataFrame with reset_index
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
print(no2_pivoted.head())


# pandas.melt() method on a DataFrame convert the data table from wide fromat to long format.
# melt all columns not mentioned in id_vars together into two columns: A column with the column header names
# and a column with the values itself.
# The reverse of pivot(long to wide format) is melt(wide to long format)
no_2 = no2_pivoted.melt(id_vars="date.utc")
print(no_2.head())

no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
print(no_2.head())







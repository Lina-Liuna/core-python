import numpy
import pandas

# in Pandas a data table is called a DataFrame.
# 1. pandas supports the integration with many file formats: csv, excel, sql, json, parquet)
# 2. importing data provided by function with the prefix read_*, to_* to store data.
# 3. method for slicing, selecting, and extracting the data you need are available in pandas
# 4. combine with Matplotlib, you can pick the plot type(scatter, bar, boxplot,...) corresponding to your data
# 5. reshape the layout of tables: melt() pivot() from long to wide format
# 6. Combine data from multiple tables
# 7. support for time series and has an extensive set of tools for working with dates,times,and time-indexed data.
# 8. Provide functions to clean textual data and extract useful information from it.

s = pandas.Series([2, 4, 6, numpy.nan, 8, 10])
print(s)

df = pandas.DataFrame(
    {
        "Name": [
            'Lina, Ms. Liu',
            'Danny, Mr. Wonderful',
            'Kanan, Mr. Hero',
        ],
        'Age':[25,35,45],
        'Sex': ['f', 'm', 'm']
    }
)
print(df)
print(df['Name'])

# pandas.DataFrame or pandas.Series provide lots of method, don't froget to use parentheses()

print(df['Age'].max())
# describe provides a quick overview of the numerical data in a DataFrame.
# df.describe return a pandas series or pandas DataFrame.
print(df.describe())

# read tabular data csv file:
# pandas.read_csv() returns DataFrame, when displaying a DataFrame, the first and last 5 rows will be shown by default.
titanic = pandas.read_csv('data/annual-financial.csv')
print(titanic)

# use the head() method with the required number of rows as argument
print(titanic.head(10))
print(titanic.tail(10))

print('-'*100)
print(titanic.dtypes)

titanic.to_excel('titanic.xlsx', sheet_name="passengers", index=False)

# use info() method to get summary of a DataFrame
print(titanic.info())

year_units = titanic[['Year', 'Units']]
print(year_units.head(11))
print(type(year_units))


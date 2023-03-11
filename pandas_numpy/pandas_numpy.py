import numpy
import pandas

# in Pandas a data table is called a DataFrame.
# 1. pandas supports the integration with many file formats: csv, excel, sql, json, parquet)
# 2. importing data provided by function with the prefix read_*, to_* to store data.
# 3. method for slicing, selecting, and extracting the data you need are available in pandas
# 4. combine with Matplotlib, you can pick the plot type(scatter, bar, boxplot,...) corresponding to your data
# 5. reshape the layout of tables:

s = pandas.Series([2, 4, 6, numpy.nan, 8, 10])
print(s)


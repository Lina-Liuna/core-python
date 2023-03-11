import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
print(titanic.head())
print(titanic["Age"].mean())
print(titanic[['Age', 'Fare']].median())
print(titanic[["Age", "Fare"]].describe())

# instead of predefined statistics, specific combinations of aggregating statistics for given columns can be defined
# using the DataFrame.agg() method

print(titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
)

# Aggregation statistics can be calculated on entire columns or rows
# groupby provides the power of the split-apply-combine pattern
# value_counts is convenient shortcut to count the number of entries in each category of a variable.
print(titanic[["Sex", "Age"]].groupby("Sex").mean())
print(titanic.groupby("Sex").mean(numeric_only=True))
print(titanic.groupby("Sex")["Age"].mean())
print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())
print(titanic["Pclass"].value_counts())
print(titanic.groupby("Pclass")["Pclass"].count())


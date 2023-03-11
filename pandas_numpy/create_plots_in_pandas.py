import pandas
import matplotlib.pyplot as plt

air_quality = pandas.read_csv('data/air_quality_no2.csv')
print(air_quality.head())
print(air_quality.describe())
print(air_quality.info)
print('-'*100)
print(air_quality.dtypes)

air_quality['station_paris'].plot()
plt.show()

air_quality.plot.scatter(x='station_paris', y='station_london', alpha=0.5)
plt.show()

air_quality.plot.box()
plt.show()


axs = air_quality.plot.area(figsize=(12,4), subplots=True)
plt.show()

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel('NO$_2$ concentration')
fig.savefig('NO$_2$ concentration.png')
plt.show()
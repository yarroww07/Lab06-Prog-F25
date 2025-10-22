import pandas as pd
import seaborn as sns 

dataset = pd.read_csv("wdi_wide.csv")

# print(dataset.info())
 
# Physician = 10 null values 
# Population = 0 null values 

# print(dataset.nunique())
# print(dataset.describe())
# It provides statistical information for each column (count, mean, standard deviation, quartiles, minimum and maximum)

dataset['GNI per capita'] = dataset['GNI']/dataset['Population']
# print(dataset['GNI per capita'].round())

# print(dataset.value_counts('Region'))
# print(dataset.value_counts('High Income Economy'))
# print(pd.crosstab(dataset['Region'], dataset['High Income Economy']))
# print(dataset.columns)


country_count = 0

filtered_data = dataset[dataset['Life expectancy, female'] > 80]
country_count = filtered_data.sum()
print(filtered_data)
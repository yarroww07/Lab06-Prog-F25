### PART 3 ###
# Question 1: What is the average international tourism per region?
# Question 2: Which sex (male vs female) has the highest life expectancy in Africa?
# Question 3: Which intermediate region has the highest GNI?
# Question 4: Do high income countries produce more greenhouse gas emissions?
# Question 5: Which continents are the most visited by tourists? Region? Subregion?
# Question 6: How is the number of physicians related to tertiary education?
# Question 7: Is a higher tertiary education for females related to high income economies? 
#             To the amount of women in national parlament?
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

### PART 4 ###

# Rania Bouladraf
# Meriem Hamzi


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

print(dataset.info())
 
# Physician = 10 null values 
# Population = 0 null values 

print(dataset.nunique())
print(dataset.describe())
# It provides statistical information for each column (count, mean, standard deviation, quartiles, minimum and maximum)

dataset['GNI per capita'] = dataset['GNI']/dataset['Population']
print(dataset['GNI per capita'].round())

print(dataset.value_counts('Region'))
print(dataset.value_counts('High Income Economy'))
print(pd.crosstab(dataset['Region'], dataset['High Income Economy']))
print(dataset.columns)


country_count = 0
filtered_data = []
for value, row in dataset.iterrows():
    if row['Life expectancy, female'] > 80:
        filtered_data += [row['Country Name']]
        country_count += 1
print('There are',country_count, 'countries with female life expectancy greater 80:')
print(filtered_data)
     




                                                   ### PART 4 ###

#1# Plot of GNI per capita vs Life Expectancy of each gender
#Females
sns.relplot(data= dataset, 
            y='Life expectancy, female', 
            x= 'GNI per capita')

#Males
sns.relplot(data= dataset,
          y='Life expectancy, male', 
          x='GNI per capita')

# Answer: The is a relationship between GNI per capita and life expectancy. The higher the life expectancy, the higher 
#         the GNI per capita. 


#2# Plot of GNI per capita vs life expectancy of each gender, depending on the region.
#Females
sns.relplot(data= dataset,
           y='Life expectancy, female', 
           x='GNI per capita',
           hue= 'Region')

#Males 
sns.relplot(data= dataset,
           y='Life expectancy, male', 
           x='GNI per capita',
           hue= 'Region')
# Answer: The association between GNI per capita and life expectancy does vary for each region. For instance, Africa seem
#         to have a lower life expectancy along with Oceania. While for Asia, it is between average and high, increasing
#         across life expectancy. While both Americas and Europe have their GNI per capita increasimg over age. 

#3#

sns.relplot(data = dataset,
            x='GNI per capita',
            y='Life expectancy, female',
            kind='line',
            hue='Region',
            errorbar='sd')

sns.relplot(data = dataset,
            x='GNI per capita',
            y='Life expectancy, male',
            kind='line',
            hue='Region',
            errorbar='sd')


#4#
sns.lmplot(data=dataset,
           x='GNI per capita',
           y='Life expectancy, female',
           hue='Region')

sns.lmplot(data=dataset,
           x='GNI per capita',
           y='Life expectancy, male',
           hue='Region')

#5#

#   Question 1: Is there a relation between female life expectancy and the level of education for females? 
sns.relplot(data = dataset, 
            x='Tertiary education, female',
            y='Life expectancy, female',
            hue='Region')

sns.relplot(data = dataset, 
            x='Tertiary education, female',
            y='Life expectancy, female',
            col='Region')

# Answer: Female life expectancy is associated with the level of tertiary education for females. A higher level of education
#         is indicative of a higher female life expectancy.

#   Question 2: Is there a relation between female life expectancy and the amount of women in national parliament?
sns.relplot(data = dataset, 
            x='Women in national parliament',
            y='Life expectancy, female',
            hue='Region')

sns.relplot(data = dataset, 
            x='Women in national parliament',
            y='Life expectancy, female',
            col='Region')
#   Answer: There does not seem to be a clear relation between female life expectancy and the amount of women in the national
#           parliament. 

#   Question 3: Is there a relation between female life expectancy and the number of physicians in a country?
sns.relplot(data = dataset, 
            x='Women in national parliament',
            y='Life expectancy, female',
            hue='Region')

sns.relplot(data = dataset, 
            x='Women in national parliament',
            y='Life expectancy, female',
            col='Region')
#   Answer: There seems to be a very slight relation between female life expectancy and the amount of physicians.

#   Question 4: Is there a relation between female life expectancy and the amount of greenhouse emissions?
sns.relplot(data = dataset, 
            x='Greenhouse gas emissions',
            y='Life expectancy, female',
            hue='Region')

sns.relplot(data = dataset, 
            x='Greenhouse gas emissions',
            y='Life expectancy, female',
            col='Region')

#   Answer: There is no relation between female life expectancy and greenhouse gas emissions.

#   Question 5: Is there a relation between female life expectancy and the usage of internet? 
sns.relplot(data = dataset, 
            x='Internet use',
            y='Life expectancy, female',
            hue='Region')

sns.relplot(data = dataset, 
            x='Internet use',
            y='Life expectancy, female',
            col='Region')

#   Answer: According to the graph, there is a relation with female life expectancy and the usage of internet. 


#6#
#a)
dataset['Emissions per capita'] = dataset['Greenhouse gas emissions']/dataset['Population'] # Adding of a new column

sns.relplot(data = dataset,
           x='Internet use', 
           y='Emissions per capita',
           hue='Region')

sns.relplot(data= dataset,
           x='Emissions per capita', 
           y='Internet use')

# Answer: Yes, there is an association between internet use and emissions per capita. In fact, as internet use increases
#         the emissions per capita increase as well.

#b)
High_emissions = dataset[dataset['Emissions per capita'] > 0.03]
print(pd.crosstab(High_emissions['Country Name'], High_emissions['Emissions per capita']))
# Answer: The countries with high emssions (above 0.03) are Brunei Darussalam (0.03799) and Qatar (0.03465)

#c)
sns.relplot(data= dataset,
           x= High_emissions['Emissions per capita'], 
           y= High_emissions['Internet use'],
           hue= High_emissions['Country Name'],
           col= High_emissions['Region'])
# Answer: There are only two countries in one region (Asia) that have high emissons, therefore there are no 
#         variations between the different region.

#d)
High_incomes = dataset[dataset['High Income Economy'] == 1]
print(pd.crosstab(High_incomes['Emissions per capita'], High_incomes['Country Name']))
print('Here are the two high economies which have high emissions')
print(High_emissions['Country Name'])
print(pd.crosstab(High_emissions['High Income Economy'], High_emissions['Emissions per capita']))

# Answer: The two countries which have high emissions are High income economies. However, this means that not all
#         High economy conutries have a high emissions.


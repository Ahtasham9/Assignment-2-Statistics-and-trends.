# -*- coding: utf-8 -*-
"""Assigment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RzZho8QpbN7oqEY-rKr7DPRcm7jdZm0Y

### Importing Important Libraries
"""

import pandas as pd # import panda library as pd for data manipulation
import matplotlib.pyplot as plt # import matplotlib as plt for data visualitzation
from matplotlib import style
import numpy as np # import nump as np
import seaborn as sns # seaborn is data visualization library build on matplotlib

"""### Implement a Function Which return Original DataFrame, Transposed DataFrames"""

def transpose(filename: str):

    # Read the file into a pandas dataframe
    dataframe = pd.read_csv(filename)

    # Transpose the dataframe
    df_transposed = dataframe.transpose()

    # Populate the header of the transposed dataframe with the header information

    # silice the dataframe to get the year as columns
    df_transposed.columns = df_transposed.iloc[1]
    # As year is now columns so we don't need it as rows
    df_transposed_year = df_transposed[0:].drop('year')

    # silice the dataframe to get the country as columns
    df_transposed.columns = df_transposed.iloc[0]

    # As country is now columns so we don't need it as rows
    df_transposed_country = df_transposed[0:].drop('country')

    return dataframe, df_transposed_country, df_transposed_year

# Passing filename to real_worldbank_data function
# will return three dataframe:
# original dataframe, transposed country as columns and transposed year as column

original_df, df_by_country, df_by_year = transpose('wb_climatechange.csv')

"""### Original DataFrame"""

# show the first 5 row
original_df.head(5)

"""### show the statistics of Original Data"""

original_df.describe() #describe method show the statistic of dataframe

"""### DataFrame In Which Countries are Columns"""

# show the first 5 row
df_by_country.head(5)

"""### DataFrame In Which Year are Columns"""

# show the first 5 row
df_by_year

"""### Create DataFrame related to Forest Area Data
### For All the countries and years
"""

# we want to see countries forest_area over specfic years
# we need to filter our original data frame to get specific fields
forest_data = original_df[['country','year','forest_area']]

# drop the null values present in the dataset
forest_data= forest_data.dropna()

"""### Get Data to Specific Years from 1990 to 2020"""

forest_data_1990 = forest_data[forest_data['year'] == 1990] # filter data related to 1990
forest_data_2000 = forest_data[forest_data['year'] == 2000] # filter data related to 2000
forest_data_2010 = forest_data[forest_data['year'] == 2010] # filter data related to 2010
forest_data_2015 = forest_data[forest_data['year'] == 2015] # filter data related to 2015
forest_data_2020 = forest_data[forest_data['year'] == 2020] # filter data related to 2020

"""### Plot Barplot"""

style.use('ggplot')

# set fig size
plt.figure(figsize=(15,10))

# set width of bars
barWidth = 0.1

# plot bar charts
plt.bar(np.arange(forest_data_1990.shape[0]),forest_data_1990['forest_area'],color='lime', width=barWidth, label='1990')
plt.bar(np.arange(forest_data_2000.shape[0])+0.2,forest_data_2000['forest_area'],color='blue',width=barWidth, label='2000')
plt.bar(np.arange(forest_data_2010.shape[0])+0.4,forest_data_2010['forest_area'],color='peru',width=barWidth, label='2010')
plt.bar(np.arange(forest_data_2015.shape[0])+0.6,forest_data_2015['forest_area'],color='yellow',width=barWidth, label='2015')
plt.bar(np.arange(forest_data_2020.shape[0])+0.8,forest_data_2020['forest_area'],color='darkviolet',width=barWidth, label='2020')

# show the legends on the plot
plt.legend()

# set the x-axis label
plt.xlabel('Country',fontsize=15)

# add title to the plot
plt.title("FOREST AREA",fontsize=15)

# add countries names to the 11 groups on the x-axis
plt.xticks(np.arange(forest_data_2020.shape[0])+0.2,('Afghanistan', 'Bangladesh', 'China', 'United Kingdom', 'India',
       'Iran, Islamic Rep.', 'Kuwait', 'Pakistan', 'Singapore', 'Ukraine',
       'United States', 'South Africa'),fontsize=10,rotation = 45)

# show the plot
plt.show()

forest_data.country.unique()

original_df.columns

"""### Get data of Agricultural land over the years"""

# we want to see countries agricultural_land over the years
# we need to filter our original data frame to get specific fields
agricultural_land = original_df[['country','year','agricultural_land']]

# drop the null values present in the dataset
agricultural_land= agricultural_land.dropna()

"""### Filter from specific year from 1990 to 2015"""

agricultural_land_1990 = agricultural_land[agricultural_land['year'] == 1990] # filter data related to 1990
agricultural_land_1995 = agricultural_land[agricultural_land['year'] == 1995] # filter data related to 1995
agricultural_land_2000 = agricultural_land[agricultural_land['year'] == 2000] # filter data related to 2000
agricultural_land_2005 = agricultural_land[agricultural_land['year'] == 2005] # filter data related to 2005
agricultural_land_2010 = agricultural_land[agricultural_land['year'] == 2010] # filter data related to 2010
agricultural_land_2015 = agricultural_land[agricultural_land['year'] == 2015] # filter data related to 2015

agricultural_land_2015.country.unique()

"""### PLOT barplot"""

style.use('ggplot')

# set fig size
plt.figure(figsize=(15,10))

# set width of bars
barWidth = 0.1

# plot bar charts
plt.bar(np.arange(agricultural_land_1990.shape[0]),
        agricultural_land_1990['agricultural_land'],
        color='lime', width=barWidth, label='1990')

plt.bar(np.arange(agricultural_land_2000.shape[0])+0.2,
        agricultural_land_2000['agricultural_land'],
        color='blue',width=barWidth, label='2000')

plt.bar(np.arange(agricultural_land_2005.shape[0])+0.4,
        agricultural_land_2005['agricultural_land'],
        color='yellow',width=barWidth, label='2005')

plt.bar(np.arange(agricultural_land_2010.shape[0])+0.6,
        agricultural_land_2010['agricultural_land'],
        color='peru',width=barWidth, label='2010')

plt.bar(np.arange(agricultural_land_2015.shape[0])+0.80,
        agricultural_land_2015['agricultural_land'],
        color='red',width=barWidth, label='2015')


# show the legends on the plot
plt.legend()

# set the x-axis label
plt.xlabel('Country',fontsize=15)

# add title to the plot
plt.title("Agricultural Land",fontsize=15)

# add countries names to the 11 groups on the x-axis
plt.xticks(np.arange(agricultural_land_2015.shape[0])+0.2,
           ('Afghanistan', 'Bangladesh', 'China', 'United Kingdom', 'India',
       'Iran, Islamic Rep.', 'Kuwait', 'Pakistan', 'Singapore', 'Ukraine',
       'United States', 'South Africa'),
             fontsize=10,rotation = 45)

# show the plot
plt.show()

agricultural_land_2015.country.unique()

"""### Making a DataFrame related to South Africa Data"""

# making dataframe of india data from the original dataframe
sa = original_df[original_df['country'] == 'South Africa']
sa.head(5)

"""### Implement a Function which removes Null values and return clean data"""

def remove_null_values(feature):
    return np.array(feature.dropna())

sa.columns

"""### For the Features Present In sa DataFrame remove the null values
### Print Each Features Size
"""

# Making dataframe of all the feature in the avaiable in
# India dataframe passing it to remove null values function
# for dropping the null values
access_to_electricity = remove_null_values(sa[['access_to_electricity']])

argicultural_land = remove_null_values(sa[['agricultural_land']])

co2_emission = remove_null_values(sa[['co2_emission']])

arable_land = remove_null_values(sa[['arable_land']])

electric_power_comsumption = remove_null_values(sa[['electric_power_comsumption']])

forest_area = remove_null_values(sa[['forest_area']])

population = remove_null_values(sa[['population_growth']])

urban_pop = remove_null_values(sa[['urban_population']])

gdp = remove_null_values(sa[['GDP']])

# find the lenght of each feature size
# this will help us in creating dataframe
# to avoid axis bound error in data frame creation
print('access_to_electricity Length = '+str(len((access_to_electricity))))
print('argicultural_land Length = '+str(len(argicultural_land)))
print('co2_emission Length = '+str(len(co2_emission)))
print('arable_land  Length = '+str(len(arable_land)))
print('electric_power_comsumption Length = '+str(len(electric_power_comsumption)))
print('forest_area Length = '+str(len(forest_area)))
print('population Length = '+str(len(population)))
print('urban_pop Length = '+str(len(urban_pop)))
print('gdp Length = '+str(len(gdp)))

"""### Make a new dataframe of clean Data(no null values) related to SA"""

# after removing the null values we will create datafram for indian data
sa_clean_data = pd.DataFrame({'access_to_electricity': [access_to_electricity [x][0] for x in range(25)],
                                 'Argicultural_land': [argicultural_land[x][0] for x in range(25)],
                                 'co2_emission ': [co2_emission [x][0] for x in range(25)],
                                 'Arable_land': [arable_land[x][0] for x in range(25)],
                                 'electric_power_comsumption ': [electric_power_comsumption [x][0] for x in range(25)],
                                 'Forest_area': [forest_area[x][0] for x in range(25)],
                                 'Population': [population[x][0] for x in range(25)],
                                 'Urban_pop': [urban_pop[x][0] for x in range(25)],
                                 'GDP': [gdp[x][0] for x in range(25)],
                                })

sa_clean_data.head(5) # call first 5 row

"""### Correlation Heatmap of India"""

# create correlation matrix
corr_matrix = sa_clean_data.corr()
plt.figure(figsize=(10,5))
# using seaborn library to create heatmap
sns.heatmap(corr_matrix, annot=True,cmap="YlGnBu")
plt.title("Correlation Heatmap of SA")
plt.show()

corr_matrix

"""### Create a dataframe contain only  Kuwait data"""

# making dataframe of Kuwait data
kw_df = original_df[original_df['country'] == 'Kuwait']
kw_df.head(5)

"""### Remove Null values from Features"""

# Making dataframe of all the feature in the avaiable in
# India dataframe passing it to remove null values function
# for dropping the null values
access_to_electricity = remove_null_values(kw_df[['access_to_electricity']])

argicultural_land = remove_null_values(kw_df[['agricultural_land']])

co2_emission = remove_null_values(kw_df[['co2_emission']])

arable_land = remove_null_values(kw_df[['arable_land']])

electric_power_comsumption = remove_null_values(kw_df[['electric_power_comsumption']])

forest_area = remove_null_values(kw_df[['forest_area']])

population = remove_null_values(kw_df[['population_growth']])

urban_pop = remove_null_values(kw_df[['urban_population']])

gdp = remove_null_values(kw_df[['GDP']])

# find the lenght of each feature size
# this will help us in creating dataframe
# to avoid axis bound error in data frame creation
print('access_to_electricity Length = '+str(len((access_to_electricity))))
print('argicultural_land Length = '+str(len(argicultural_land)))
print('co2_emission Length = '+str(len(co2_emission)))
print('arable_land  Length = '+str(len(arable_land)))
print('electric_power_comsumption Length = '+str(len(electric_power_comsumption)))
print('forest_area Length = '+str(len(forest_area)))
print('population Length = '+str(len(population)))
print('urban_pop Length = '+str(len(urban_pop)))
print('gdp Length = '+str(len(gdp)))

"""### Create a new DataFrame for Kuwait data contain no null values"""

# after removing the null values we will create datafram for indian data
kw_clean_data = pd.DataFrame({'Argicultural_land': [argicultural_land[x][0] for x in range(22)],
                                 'co2_emission ': [co2_emission [x][0] for x in range(22)],
                                 'Arable_land': [arable_land[x][0] for x in range(22)],
                                 'electric_power_comsumption ': [electric_power_comsumption [x][0] for x in range(22)],
                                 'Forest_area': [forest_area[x][0] for x in range(22)],
                                 'Population': [population[x][0] for x in range(22)],
                                 'Urban_pop': [urban_pop[x][0] for x in range(22)],
                                 'GDP': [gdp[x][0] for x in range(22)],
                                })

"""### Correlation Heatmap of Kuwait"""

# create correlation matrix
corr_matrix = kw_clean_data.corr()
plt.figure(figsize=(10,5))
# using seaborn library to create heatmap
sns.heatmap(corr_matrix, annot=True,cmap="Blues")
plt.title("Correlation Heatmap of Kuwait")
plt.show()

corr_matrix

"""### Make dataframe of United States data from the original dataframe"""

# making dataframe of Iran data from the original dataframe
us_df = original_df[original_df['country'] == 'United States']
us_df.head(5)

"""### For the Features Present In United States DataFrame remove the null values
### Print Each Features Size
"""

# Making dataframe of all the feature in the avaiable in
# India dataframe passing it to remove null values function
# for dropping the null values
access_to_electricity = remove_null_values(us_df[['access_to_electricity']])

argicultural_land = remove_null_values(us_df[['agricultural_land']])

co2_emission = remove_null_values(us_df[['co2_emission']])

arable_land = remove_null_values(us_df[['arable_land']])

electric_power_comsumption = remove_null_values(us_df[['electric_power_comsumption']])

forest_area = remove_null_values(us_df[['forest_area']])

population = remove_null_values(us_df[['population_growth']])

urban_pop = remove_null_values(us_df[['urban_population']])

gdp = remove_null_values(us_df[['GDP']])

# find the lenght of each feature size
# this will help us in creating dataframe
# to avoid axis bound error in data frame creation
print('access_to_electricity Length = '+str(len((access_to_electricity))))
print('argicultural_land Length = '+str(len(argicultural_land)))
print('co2_emission Length = '+str(len(co2_emission)))
print('arable_land  Length = '+str(len(arable_land)))
print('electric_power_comsumption Length = '+str(len(electric_power_comsumption)))
print('forest_area Length = '+str(len(forest_area)))
print('population Length = '+str(len(population)))
print('urban_pop Length = '+str(len(urban_pop)))
print('gdp Length = '+str(len(gdp)))

"""### Make a new dataframe of clean Data(no null values) related to United States"""

# after removing the null values we will create datafram for indian data
us_clean_data = pd.DataFrame({'Argicultural_land': [argicultural_land[x][0] for x in range(24)],
                                 'co2_emission ': [co2_emission [x][0] for x in range(24)],
                                 'Arable_land': [arable_land[x][0] for x in range(24)],
                                 'electric_power_comsumption ': [electric_power_comsumption [x][0] for x in range(24)],
                                 'Forest_area': [forest_area[x][0] for x in range(24)],
                                 'Population': [population[x][0] for x in range(24)],
                                 'Urban_pop': [urban_pop[x][0] for x in range(24)],
                                 'GDP': [gdp[x][0] for x in range(24)],
                                })

"""### Correlation Heatmap of US Data Features"""

# create correlation matrix
corr_matrix = us_clean_data.corr()
plt.figure(figsize=(10,5))
# using seaborn library to create heatmap
sns.heatmap(corr_matrix, annot=True,cmap="Greens")
plt.title("Correlation Heatmap of US Data Features")
plt.show()

corr_matrix

original_df.columns

"""### Get the Year, Country Data Related to Co2 Emission"""

# we want to see countries greenhouse_gas_emissions over the years
# we need to filter our original data frame to get specific fields
co2_emission_df = original_df[['country','year','co2_emission']]

# drop the null values present in the dataset
co2_emission_df= co2_emission_df.dropna()

co2_emission_df.country.unique() # shows the all the countries in country features

"""### Filter the Data For All the Countries"""

Agf_emission = co2_emission_df[co2_emission_df['country'] == 'Afghanistan']
ban_emission = co2_emission_df[co2_emission_df['country']== 'Bangladesh']
chn_emission =  co2_emission_df[co2_emission_df['country'] == 'China']
Ind_emission = co2_emission_df[co2_emission_df['country'] == 'India']
Iran_emission = co2_emission_df[co2_emission_df['country'] == 'Iran, Islamic Rep.']
Kuw_emission = co2_emission_df[co2_emission_df['country'] == 'Kuwait']
Pak_emission = co2_emission_df[co2_emission_df['country'] == 'Pakistan']
ukn_emission = co2_emission_df[co2_emission_df['country'] == 'United Kingdom']
sing_emission = co2_emission_df[co2_emission_df['country'] == 'Singapore']
Ukr_emission = co2_emission_df[co2_emission_df['country'] == 'Ukraine']
SA_emission = co2_emission_df[co2_emission_df['country'] == 'South Africa']
NZ_emission = co2_emission_df[co2_emission_df['country']== 'New Zealand']

"""### Line Plot of Co2 Emission"""

# set fig size
plt.figure(figsize=(15,10))

# set the line plot value on x-axis and y-axis by year and co2 emission respectively
plt.plot(Agf_emission.year, Agf_emission.co2_emission, ':',label='Afghanistan')
plt.plot(ban_emission.year, ban_emission.co2_emission,':',label='Bangladesh')
plt.plot(chn_emission.year, chn_emission.co2_emission,':',label='China')
plt.plot(Ind_emission.year, Ind_emission.co2_emission,'-r',label='India')
plt.plot(Iran_emission.year, Iran_emission.co2_emission,'--b',label='Iran')
plt.plot(Kuw_emission.year, Kuw_emission.co2_emission,':',label='Kuwait')
plt.plot(Pak_emission.year, Pak_emission.co2_emission,':g',label='Pakistan')
plt.plot(ukn_emission.year, ukn_emission.co2_emission,':',label='United Kingdom')
plt.plot(sing_emission.year, sing_emission.co2_emission,':c',label='Singapore')
plt.plot(Ukr_emission.year, Ukr_emission.co2_emission,':k',label='Ukraine')
plt.plot(SA_emission.year, SA_emission.co2_emission,':r',label='South Africa')
plt.plot(NZ_emission.year, NZ_emission.co2_emission,':',label='New Zealand')

#Set the X-axis label and make it bold
plt.xlabel('Year',fontweight='bold')

# set the title
plt.title("Co2 Emission")

# show the legends on the plot and place it on suitable position
plt.legend(bbox_to_anchor=(0.89,0.6),shadow=True)

#show the line plot
plt.show()



"""### Get the Year, Country Data Related to Arable Land"""

# we want to see countries arable_land over the years
# we need to filter our original data frame to get specific fields
arable_land_df = original_df[['country','year','arable_land']]

# drop the null values present in the dataset
arable_land_df= arable_land_df.dropna()

"""### Filter the Data For All the Countries"""

Agf_arable_land = arable_land_df[arable_land_df['country'] == 'Afghanistan']
ban_arable_land = arable_land_df[arable_land_df['country']== 'Bangladesh']
chn_arable_land =  arable_land_df[arable_land_df['country'] == 'China']
Ind_arable_land = arable_land_df[arable_land_df['country'] == 'India']
Iran_arable_land = arable_land_df[arable_land_df['country'] == 'Iran, Islamic Rep.']
Kuw_arable_land = arable_land_df[arable_land_df['country'] == 'Kuwait']
Pak_arable_land = arable_land_df[arable_land_df['country'] == 'Pakistan']
ukn_arable_land = arable_land_df[arable_land_df['country'] == 'United Kingdom']
sing_arable_land = arable_land_df[arable_land_df['country'] == 'Singapore']
Ukr_arable_land = arable_land_df[arable_land_df['country'] == 'Ukraine']
SA_arable_land = arable_land_df[arable_land_df['country'] == 'South Africa']
NZ_arable_land = arable_land_df[arable_land_df['country']== 'New Zealand']

"""### Line Plot of arable_land"""

# set fig size
plt.figure(figsize=(15,10))
# set the line plot value on x-axis and y-axis by year and co2 emission respectively
plt.plot(Agf_arable_land.year, Agf_arable_land.arable_land, ':',label='Afghanistan')
plt.plot(ban_arable_land.year, ban_arable_land.arable_land,':',label='Bangladesh')
plt.plot(chn_arable_land.year, chn_arable_land.arable_land,':',label='China')
plt.plot(Ind_arable_land.year, Ind_arable_land.arable_land,'-r',label='India')
plt.plot(Iran_arable_land.year, Iran_arable_land.arable_land,'--b',label='Iran')
plt.plot(Kuw_arable_land.year, Kuw_arable_land.arable_land,':',label='Kuwait')
plt.plot(Pak_arable_land.year, Pak_arable_land.arable_land,':g',label='Pakistan')
plt.plot(ukn_arable_land.year, ukn_arable_land.arable_land,':',label='United Kingdom')
plt.plot(sing_arable_land.year, sing_arable_land.arable_land,':c',label='Singapore')
plt.plot(Ukr_arable_land.year, Ukr_arable_land.arable_land,':k',label='Ukraine')
plt.plot(SA_arable_land.year, SA_arable_land.arable_land,':r',label='South Africa')
plt.plot(NZ_arable_land.year, NZ_arable_land.arable_land,':',label='New Zealand')

#Set the X-axis label and make it bold
plt.xlabel('Year',fontweight='bold')

# set the title
plt.title("Arable Land")

# show the legends on the plot and place it on suitable position
plt.legend(bbox_to_anchor=(0.15,0.5),shadow=True)

#show the line plot
plt.show()

original_df.columns

# we want to see countries electric_power_comsumption over the years
electric_power_comsumption = original_df[['country','year','electric_power_comsumption']]

# drop the null values present in the dataset
electric_power_comsumption= electric_power_comsumption.dropna()

"""### Filter from specific year from 1990 to 2015"""

# filter data related to 1990
electric_power_comsumption_1990 = electric_power_comsumption[electric_power_comsumption['year'] == 1990]

# filter data related to 2010
electric_power_comsumption_2010 = electric_power_comsumption[electric_power_comsumption['year'] == 2010]

electric_power_comsumption_1990

electric_power_comsumption_2010
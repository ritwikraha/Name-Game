#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
# Reading in datasets/nytkids_yearly.csv, which is semicolon delimited.
# ...YOUR CODE FOR TASK 2...
author_df= pd.read_csv('nytkids_yearly.csv', sep=';')
# Looping through author_df['Author'] to extract the authors first names
first_name = []
author_df['Author']
for name in author_df['Author']:
    first_name.append(name.split(" ")[0])

# Adding first_name as a column to author_df
# ...YOUR CODE FOR TASK 2...
author_df['first_name']= first_name

# Checking out the first few rows of author_df
# ...YOUR CODE FOR TASK 2...
author_df.head()


# In[4]:


import numpy as np
# Looping through author's first names to create the nysiis (fuzzy) equivalent
nysiis_name = []
# ...YOUR CODE FOR TASK 3...
for name in author_df['first_name']:
    nysiis_name.append(fuzzy.nysiis(name))

# Adding nysiis_name as a column to author_df
# ...YOUR CODE FOR TASK 3...
author_df['nysiis_name']= nysiis_name
# Printing out the difference between unique firstnames and unique nysiis_names:
# ...YOUR CODE FOR TASK 3...
print(len(np.unique(author_df['first_name'])) - len(np.unique(author_df['nysiis_name'])))


# In[5]:


# Reading in datasets/babynames_nysiis.csv, which is semicolon delimited.
babies_df = pd.read_csv('babynames_nysiis.csv', sep=';')
print(babies_df.head())
# Looping through babies_df to and filling up gender
gender = []
# ... YOUR CODE FOR TASK 4 ...
for x,y in zip(babies_df['perc_female'], babies_df['perc_male']):
    if x>y:
        gender.append('F')
    elif x<y:
        gender.append('M')
    else:
        gender.append("N")
# Adding a gender column to babies_df
# ... YOUR CODE FOR TASK 4 ...
babies_df['gender']=gender
# Printing out the first few rows of babies_df
# ... YOUR CODE FOR TASK 4 ...
babies_df.head()


# In[6]:


# This function returns the location of an element in a_list.
# Where an item does not exist, it returns -1.
def locate_in_list(a_list, element):
    loc_of_name = a_list.index(element) if element in a_list else -1
    return(loc_of_name)

# Looping through author_df['nysiis_name'] and appending the gender of each
# author to author_gender.
author_gender = []
# ...YOUR CODE FOR TASK 5...
for name in author_df['nysiis_name']:
    ind = locate_in_list(list(babies_df['babynysiis']), name)
    if ind<0:
         author_gender.append('Unknown')
    else:
        author_gender.append(babies_df['gender'][locate_in_list(list(babies_df['babynysiis']), name)])
print(author_gender)
# Adding author_gender to the author_df
# ...YOUR CODE FOR TASK 5...
author_df['author_gender']=author_gender
# Counting the author's genders
# ...YOUR CODE FOR TASK 5...
author_df.head()


# In[7]:


# Creating a list of unique years, sorted in ascending order.
years = sorted(author_df['Year'].unique())

# Initializing lists
males_by_yr = []
females_by_yr = []
unknown_by_yr = []

# Looping through years to find the number of male, female and unknown authors per year
# ...YOUR CODE FOR TASK 6...
for year in years:
    df= author_df[author_df['Year']==year]
    males_by_yr.append(len( df[ df['author_gender']=='M' ] ))
    females_by_yr.append(len( df[ df['author_gender']=='F' ] ))
    unknown_by_yr.append(len( df[ df['author_gender']=='Unknown' ] ))

# Printing out yearly values to examine changes over time
# ...YOUR CODE FOR TASK 6...
print(males_by_yr, females_by_yr, unknown_by_yr)


# In[8]:


# Importing matplotlib
import matplotlib.pyplot as plt

# This makes plots appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Plotting the bar chart
# ...YOUR CODE FOR TASK 7...
plt.bar(years, unknown_by_yr)
# [OPTIONAL] - Setting a title, and axes labels
# ...YOUR CODE FOR TASK 7...
plt.title('unknown in each year')
plt.xlabel('year')
plt.ylabel('no. of unknowns')


# In[10]:


# Creating a new list, where 0.25 is added to each year
years_shifted = [x+0.25 for x in years]
print(years_shifted)

# Plotting males_by_yr by year
# ... YOUR CODE FOR TASK 8 ...
plt.bar(years, males_by_yr,width=0.25, color='blue')

# Plotting females_by_yr by years_shifted
# ... YOUR CODE FOR TASK 8 ...
plt.bar(years_shifted, females_by_yr,width=0.25, color='red')
# [OPTIONAL] - Adding relevant Axes labels and Chart Title
# ... YOUR CODE FOR TASK 8 ...


# In[ ]:





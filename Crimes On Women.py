#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


data = pd.read_csv(r'C:\Users\swastika\OneDrive\Desktop\Dataset\CrimesOnWomenData.csv')


# In[12]:


print("Basic Info:")
print(data.info())


# In[13]:


print("\nFirst 5 rows:")
print(data.head())


# In[14]:


print("\nMissing values in each column:")
print(data.isnull().sum())


# In[9]:


print("\nDescriptive statistics:")
print(data.describe())


# In[15]:


if 'TotalCrimes' in data.columns:
    total_crimes = data['TotalCrimes'].sum()
    print(f"\nTotal number of crimes: {total_crimes}")


# In[16]:


if 'Year' in data.columns:
    crimes_per_year = data.groupby('Year')['TotalCrimes'].sum()
    print("\nCrimes per year:")
    print(crimes_per_year)


# In[19]:


plt.figure(figsize=(10, 6))
crimes_per_year.plot(kind='bar')
plt.title('Crimes Per Year')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.show()


# In[34]:


if 'State' in data.columns:
    crimes_per_region = data.groupby('State')['TotalCrimes'].sum()
    print("\nCrimes per region:")
    print(crimes_per_region)


# In[35]:


plt.figure(figsize=(10, 6))
crimes_per_region.plot(kind='bar', color='skyblue')
plt.title('Crimes Per Region')
plt.xlabel('State')
plt.ylabel('TotalCrimes')
plt.xticks(rotation=45)
plt.show()


# In[23]:


if 'Year' in data.columns and 'Rape' in data.columns:
    rape_trend = data.groupby('Year')['Rape'].sum()
    print("\nRape cases per year:")
    print(rape_trend)


# In[26]:


plt.figure(figsize=(10, 6))
rape_trend.plot(kind='line', marker='o', color='red')
plt.title('Rape Cases Per Year')
plt.xlabel('Year')
plt.ylabel('Total Rape Cases')
plt.grid(True)
plt.show()


# In[27]:


plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between different crime types')
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing Exercise

# #### Q4. TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences
# 

# In[24]:


import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency


# In[4]:


df = pd.read_csv('Orderform.csv')
df.head()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[16]:


df.Phillippines.value_counts()


# In[17]:


df.Indonesia.value_counts()


# In[18]:


df.Malta.value_counts()


# In[44]:


df.India.value_counts()


# In[23]:


matrix = np.array([[271,267,269,280],[29,33,31,20]])
matrix


# In[43]:


chi2 , p , dof, expected = chi2_contingency(matrix)
print(f"Test statistic  {chi2:}")
print(f"P-value  {p}")
print(f"degrees of freedom  {dof:}")
print("Expected values")


# #### According to the chi-square table, critical value for dof =3 and alpha= 0.05 is 7.815.Comparing the Critical value = 7.815 and Test statistic value = 3.8589.Therfore, chi-square calculated value is less than the chi-square critical value,Also p-value is significantly greater than 0.05. thus we fail to reject the null hypothesis. 

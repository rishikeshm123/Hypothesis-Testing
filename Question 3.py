#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Test exercise

# #### Q3. Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.
# 

# In[32]:


import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy import chi2_contingency


# In[29]:


df = pd.read_csv('BuyerRatio.csv',index_col=0)
df


# ##### As we have categorical variables, we will move forward using Chi-square test.

# In[18]:


#H0 =  All proportions are equal
#H1 =  Not all Proportions are equal


# In[37]:


chi2, p, dof, expected = chi2_contingency(df)

print(f"Test statistic:     {chi2:}")
print(f"p-value:            {p:}")
print(f"degrees of freedom: {dof}")
print("expected frequencies:")
print(expected)


# #### According to the chi-square table, critical value for dof =3 and alpha= 0.05 is 7.815.Comparing the Critical value = 7.815 and Test statistic value = 1.5959.Therfore, chi-square calculated value is less than the chi-square critical value,Also p-value is significantly greater than 0.05. thus we fail to reject the null hypothesis. 
# 

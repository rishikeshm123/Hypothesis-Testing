#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Test Excercise

# #### A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch. Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
# 

# In[7]:


import pandas as pd
import numpy as np
import scipy.stats as stats


# In[5]:


lab = pd.read_csv('labTAT.csv')
lab.head()


# In[6]:


lab.shape


# ##### As we have 4 groups to compare, we will use ANOVA. 
# ##### First, we will assume null and alternate hypothesis.

# In[ ]:


#H0 (Null Hypthesis) : µ1 = µ2 = µ3 = µ4 
#H1 (Alternate hypothesis) : Atleast one mean is different.                                                         


# In[13]:


print("P_Value :{0}".format(stats.f_oneway(lab.iloc[:,0],lab.iloc[:,1],lab.iloc[:,2],lab.iloc[:,3])[1]))


# ##### As we can see p-value is significantly smaller than 0.05, We will Accept the alternate hypothesis and reject the null hypothesis.
# Therefore, we can conclude that there is significant difference between atleast one of the TAT reports.

# In[ ]:





# In[ ]:





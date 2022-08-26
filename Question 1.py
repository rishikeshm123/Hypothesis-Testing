#!/usr/bin/env python
# coding: utf-8

# #                                            Hypothesis Testing Exercise

# ##### Q1.      A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
# 

# In[1]:


import pandas as pd
import numpy as np
import scipy.stats as stats


# In[6]:


cutlets = pd.read_csv('cutlets.csv')
cutlets.head()


# In[11]:


cutlets.shape


# In[9]:


cutlets.describe()


# ### Step 1: Define null and alternate hypothesis

# In[ ]:


#H0 :diameter of A = diameter of B, µ1 = µ2
#H1 :diameter of A ≠  diameter of B, u1 ≠ u2


# In[20]:


UA= cutlets.loc[:,'Unit A']
UA.head()


# In[22]:


UB = cutlets.loc[:,"Unit B"]
UB.head()


# In[23]:


#As the sample here is same ie. cutlet diameter, We will conduct two sample t test.
stats.ttest_ind(UA,UB)


# ##### As p value > 0.05 we will reject alternate hypothesis and accept null hypothesis. That means, there is no significant difference in diameters of Unit A and Unit B.

# In[ ]:





# In[ ]:





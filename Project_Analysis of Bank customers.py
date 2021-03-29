#!/usr/bin/env python
# coding: utf-8

# In[292]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[293]:


loan_data = pd.read_csv('C:\\Users\\hemfa\\Downloads\\Customers_of_Bank.csv')


# In[294]:


type(loan_data)


# In[295]:


loan_data = pd.read_csv('C:\\Users\\hemfa\\Downloads\\Customers_of_Bank.csv')

loan_data.drop(columns=['ID'], axis=1, inplace=True)
loan_data.rename(columns={"Experience": "Work_experience", "CCAvg": "Avg_credit_card_monthly",
                   "Mortgage": "Mortgage_value_k", "Personal Loan": "Accepted_personal_loan",
                   "ZIP Code": "ZIP_Code", "Online": "Online_transactions"}, inplace=True)
loan_data['Total_bank_relationships'] = (loan_data['Accepted_personal_loan'] + loan_data['Securities Account'] +
                                         loan_data['CreditCard'] + loan_data['Online_transactions'])

loan_data.head()


# In[296]:


loan_data.shape


# In[297]:


loan_data.describe()


# avg age = 45, min and max  = 23 and 67
# avg income = $73

# In[298]:


loan_data.info()


# In[299]:


loan_data.isnull()


# In[300]:


loan_data.isnull().sum()


# In[301]:


neg_Workexp = loan_data.Work_experience < 0
neg_Workexp.value_counts()


# In[302]:


# loan_data.abs(column = ['Work_experience'], inplace=True)

# loan_data.loc[loan_data.Work_experience.abs(), inplace = True]

# loan_data.Work_experience = abs(Work_experience)
# loan_data.Work_experience = loan_data['Work_experience'].abs()
# loan_data['Work_experience']=loan_data['Work_experience'].abs()
# loan_data[loan_data['Work_experience'] < 0]['Work_experience'].abs()
loan_data.Work_experience = abs(loan_data.Work_experience)


# In[303]:


loan_data[loan_data['Work_experience'] < 0]['Work_experience'].count()


# In[304]:


loan_data.Work_experience = pd.to_numeric(loan_data.Work_experience)


# In[305]:


loan_data.describe()


# min work_experience is 0 contrary to the previous data of -3

# In[306]:


quantitivecor = ['Age', 'Education', 'Income', 'Income', 'Avg_credit_card_monthly', 'Mortgage_value_k']
experience_Grid = sns.PairGrid(loan_data, y_vars = 'Work_experience', x_vars = quantitivecor)
experience_Grid.map(sns.regplot)


# The higher the age and education level, the longer work experience. This means bank can offer loans to the elder 
# customers with advanced professional experience.

# In[307]:


def summary(values):
    values_min = loan_data[values].min()
    values_max = loan_data[values].max()
    q1 = loan_data[values].quantile(0.25)
    q2 = loan_data[values].quantile(0.50)
    q3 = loan_data[values].quantile(0.75)
    print(f'5 Point Summary of {values.capitalize()} Attribute:\n'
          f'{values.capitalize()}(min) : {values_min}\n'
          f'q1                    : {q1}\n'
          f'q2(Median)            : {q2}\n'
          f'q3                    : {q3}\n'
          f'{values.capitalize()}(max) : {values_max}')

    fig = plt.figure(figsize=(16, 10))
    plt.subplots_adjust(hspace = 0.6)
    sns.set_palette('pastel')
    
    plt.subplot(221)
    ax1 = sns.distplot(loan_data[values], color = 'r')
    plt.title(f'{values.capitalize()} Distribution')
    
    plt.subplot(222)
    ax2 = sns.violinplot(loan_data[values], palette = 'Accent', split = True)
    plt.title(f'{values.capitalize()} Violinplot')
    
    plt.subplot(223)
    ax2 = sns.boxplot(loan_data[values], palette = 'cool', width=0.7, linewidth=0.6)
    plt.title(f'{values.capitalize()} Boxplot')
    
    plt.subplot(224)
    ax3 = sns.kdeplot(loan_data[values], cumulative=True)
    plt.title(f'{values.capitalize()} Cumulative Density Distribution')
    
    plt.show()


# In[308]:


summary('Age')


# In[309]:


summary('Work_experience')


# The experience is normally distributed

# In[310]:


summary('Income')


# In[311]:


# sns.distplot(loan_data['Income'], color = 'red')
# plt.title('Income')


income=loan_data['Income'].value_counts().head(30)
ax=income.plot.bar(width=0.5,color="indigo") 
plt.xlabel("Income in Dollar")
plt.ylabel("Count")
for i, j in income.reset_index().iterrows():
    ax.text(i, j.Income + 1.5, j.Income, color='blue',rotation=90)


# The distribution is higher than normal, which is positive 

# In[312]:


sns.countplot(loan_data['Family'])
plt.title('Family size')


# Most of the customers have family member of 1․ 
# Customers with family size of 3 are comparatively less․

# In[313]:


sns.distplot(loan_data['Avg_credit_card_monthly'])
plt.title('Average monthly spending on credit cards')


# Most of the customers average monthly spending on credit cards is between 0 $ to 2000 $. 
# There are very few customers whose monthly spending is between $ 8000  - $ 10000.

# In[314]:


sns.countplot(loan_data['Education'])
plt.title('Education levels')


# 1 = Undergraduate, 2 = Graduate, 3 =Advanced/Professional․ 
# Majority of customers has only undergraduate degree.

# In[315]:


loan_data_cc = loan_data['CreditCard']
loan_data_cc = loan_data_cc.astype({'CreditCard': 'float64'})
sns.distplot(loan_data_cc)


# Those who do not own credit card are half as many as credit card holders.

# In[316]:


sns.distplot(loan_data['Total_bank_relationships'])
plt.title('Total_bank_relationships')


# According to the graph most of the customers use only one service of the bank and no one uses 4 services.

# In[317]:


n_true = len(loan_data.loc[loan_data['Accepted_personal_loan'] == True])
n_false = len(loan_data.loc[loan_data['Accepted_personal_loan'] == False])
print('Number of customers who accepted the Loan offer: {0} ({1:2.2f}%)'
      .format(n_true, (n_true / (n_true + n_false)) * 100))
print('Number of customers who did not accept the Loan offer: {0} ({1:2.2f}%)'
      .format(n_false, (n_false / (n_true + n_false)) * 100))


# In[318]:


loan_acceptance_count = pd.DataFrame(loan_data['Accepted_personal_loan'].value_counts()).reset_index()
loan_acceptance_count.columns = ['Labels', 'Accepted_personal_loan']
loan_acceptance_count


# In[319]:


pie_labels = loan_acceptance_count['Labels']
pie_labels = ['Not Accepted' if i == 0 else 'Accepted' for i in pie_labels]
  
pie_loan_data = loan_acceptance_count['Accepted_personal_loan'] 

explode = (0, 0.15)
fig, ax = plt.subplots(figsize =(12, 6))
wp = {}
def func(pct, allvalues): 
    absolute = int(np.round(pct / 100.*np.sum(allvalues)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


ax.pie(pie_loan_data,  
       autopct = lambda pct: func(pct, pie_loan_data), 
       labels = pie_labels, 
       explode = explode, 
       startangle = 50, 
       wedgeprops = wp)


plt.title('Acceptance of Personal Loans', size=15)


# In[320]:


sns.displot(x ='Education', data = loan_data, hue = 'Accepted_personal_loan')
plt.title('Influence of education on loan acceptance')


# There is a slight influence of education on loan acceptance, as most of the customers with undergraduate
# degree did not accept the offered loan. However, the majority of customers who accepted the loans holds advanced
# degree level.

# In[321]:


sns.boxplot( x ='Education', y='Income', hue='Accepted_personal_loan', data=loan_data)


# Customers who accepted the loans had the same income level, in spite of those who did not accept.

# In[322]:


sns.boxplot(x='CreditCard', y = 'Mortgage_value_k', hue = 'Accepted_personal_loan', data=loan_data)


# The customers who have accepted the offered loans have higher mortgage debt and hold credit cards. 

# In[323]:


loan_data.corr()


# In[324]:


plt.figure(figsize = (15, 8))
plt.title('Correlation of factors', y=1, size=15)
sns.heatmap(loan_data.corr(), annot = True, fmt='.2f')


# The correlation matrix illustrated high correlation between customers' income and their average monthly 
# spending on credit cards. Obviously there is the highest correlation between age and work experience 
# of customers. Interestingly, there is a strong correlation relationship between the users of total bank services 
# and credit card holders, suggesting that if the bank focuses on credit card holders and attracts perpective 
# customers using cc, it can increase the number of customers and turn them lenders.

# In[ ]:





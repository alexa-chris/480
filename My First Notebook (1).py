
# coding: utf-8

# # my first notebook

# In[7]:


print ('my first notebook')


# In[8]:


1+2


# In[9]:


a = 3


# In[12]:


print (a)


# In[13]:


pip install xlrd


# In[15]:


get_ipython().system('pip install xlrd')


# In[17]:


import xlrd
book = xlrd.open_workbook("Diamonds.xls")
sheet = book.sheet_by_name("Diamonds")


# In[18]:


for row_index in range(1,5): # read the first 4 rows, skip the first row
    id_, weight, color,_,_,price = sheet.row_values(row_index)
    print(id_,weight,color,price)


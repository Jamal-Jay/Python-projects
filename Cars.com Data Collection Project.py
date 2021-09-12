#!/usr/bin/env python
# coding: utf-8

# In[67]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import re


# In[84]:


price= []
mkmodel = []
mileage= []
year = []


# In[41]:


url = "https://www.cars.com/shopping/results/?page=1&page_size=100&list_price_max=&makes[]=&maximum_distance=20&models[]=&stock_type=used&zip=53151"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
           "Accept-Encoding":"gzip, deflate",  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


# In[83]:


def pagelooper(n,m):
    for i in range(n,m):
        while(1):
            try:
                page = requests.get(f"""https://www.cars.com/shopping/results/?page={i}&page_size=100&list_price_max=&makes[]
                =&maximum_distance=20&models[]=&stock_type=used&zip=53151""",headers=headers)

                soup1 = BeautifulSoup(page.content,"html.parser")
                soup2= BeautifulSoup(soup1.prettify(),'html.parser')
                search = soup2.find_all(class_="primary-price")
                search2 = soup2.find_all(class_="title")
                search3 = soup2.find_all(class_='mileage')
            except AttributeError:
                print('Retrying')
                time.sleep(3)
            else:
                break
        for i,j,k in zip(search,search2,search3,):
            price.append(i.get_text().strip())
            year.append(j.get_text().strip()[0:4])
            mkmodel.append(j.get_text().strip()[5:])
            mileage.append(k.get_text().strip())
        time.sleep(6)
        v +=1
        print(f"Page {v} scanned...")


# In[85]:


pagelooper(1,40)


# In[6]:


import datetime
today = datetime.date.today()
print(today)


# In[86]:


cardata= list(zip(price,year,mkmodel,mileage))


# In[50]:


cardata


# In[87]:


need = pd.DataFrame(cardata,columns=['price','year','mkmodel','mileage'])


# In[100]:


need


# In[101]:


need.to_csv('carscom.csv')


# In[59]:


getcount = requests.get("""https://www.cars.com/shopping/results/?page=1&page_size=100&list_price_max=&makes[]
                =&maximum_distance=20&models[]=&stock_type=used&zip=53151""",headers=headers)
setup1 = BeautifulSoup(page.content,"html.parser")
setup2 = BeautifulSoup(soup1.prettify(),'html.parser')
pagecounter = setup2.find(class_="total-filter-count").get_text()


# In[82]:


x =  ''.join(re.findall(r"\d+", pagecounter.strip()))


# In[80]:


int(x)//100


# In[91]:


pd.ExcelWriter('Cars.com used info.xlsx').save()


# In[102]:





# In[ ]:





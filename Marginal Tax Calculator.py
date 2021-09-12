#!/usr/bin/env python
# coding: utf-8

# In[2]:


def m_income(wage,hours,extra=0):
    income = wage*hours*52
    deduc = income - 12550
    if deduc<0:
        fcost = 0
    elif 0<deduc<=9950:
        fcost = 0.10*deduc
    elif 9950<deduc<=40525:
        fcost= 995+ (deduc-9950)*0.12
    elif 40525<deduc<=86375:
        fcost = 4664+ (deduc- 40525)*0.22
    else:
        fcost =14751+ (deduc-86375)*0.24
    if 0<income<=11970:
        scost = income*0.0354
    elif 11970<income<=23930:
        scost = 423.74 + (income-11970)*0.0465
    else:
        scost = 979.88 + (income-23930)*0.0627
    fica = income*0.0765
    final_income = income + extra - round(fcost+ scost+fica)
    print(f"Federal liability: ${round(fcost)}")
    print(f"State Liability: ${round(scost)}")
    print(f"FICA liability: ${round(fica)}")
    print(f"Yearly Income: ${round(final_income)}")
    print(f"Monthly Income: ${round((final_income)/12)}")


# In[3]:


m_income(18.89,24,2000)


# In[ ]:





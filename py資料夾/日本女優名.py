#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time
import random
from bs4 import BeautifulSoup

start=1 #起始頁面
times=100 #抓取頁數
end=start+times #終止頁數

for i in range(start,end,1):
    link="https://www.jav321.com/stars/"+str(i)
    jav = requests.get(link)
    time.sleep(1)
    soup = BeautifulSoup(jav.text,"html.parser")
    name = soup.find_all("h4")
    print("page"+str(i),"\n")
    for a in name:
        print(a.text)
    print("\n")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time
from bs4 import BeautifulSoup
import random
start=1 #起始頁面
times=10 #抓取頁數
end=start+times #終止頁數

for i in range(start,end,1):
    link="https://www.jav321.com/star/6644/"+str(i)
    jav = requests.get(link)
    time.sleep(random.randint(1,10))
    soup = BeautifulSoup(jav.text,"html.parser")
    name = soup.find_all("a")
    for a in name:
        if(len(a.text.split())>1 and a.text!="← 前の" and a.text!="→ 次の"):
            print(a.text)


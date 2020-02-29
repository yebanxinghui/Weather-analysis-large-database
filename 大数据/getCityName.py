import requests                                                                      
from bs4 import BeautifulSoup 
import pandas as pd
import time
import os

path = r"D:\\Programs\\Python_Programs\\hello\\Projects\\数据集处理\\delete_data\\"
filenames = os.listdir(path)

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"}                                                                                                                                                  
count_spider = 0

url = "https://lishi.tianqi.com"
response = requests.get(url, headers=headers)
sym_list = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'b', 'h', 'j', 'l', 'q', 's', 't', 'y']
soup = BeautifulSoup(response.text, 'html.parser') 
ul_all=soup.find_all("ul",{"class":"bcity"})

start_list = ['A', 'D', 'G', 'J', 'M', 'P', 'S', 'W', 'end']


#################################################
######################修改此处###################
each_person = 3#分组爬取，组数为start_list索引范围
######################修改此处###################
#################################################

# 获取全部城市名称和url
city_all = []
city_url = []
flag_start = True
for i in ul_all: 
    li_all=i.find_all("li")
    for j in li_all:
        if flag_start:
            if j.text != start_list[each_person]:
                continue
            else:
                flag_start = False
                continue
        else:
            if j.text == start_list[each_person + 1]:
                flag_start = True
                continue
                        
            if j.text in sym_list:
                continue
            city_url.append(j.a.get('href'))
            city_all.append(j.text)
print(city_all)
print(len(city_all))

count = 0
for url in city_url:

    start_time = time.time()
    if url is "#":
        count += 1
        continue
    # print(url)
    csv_name = city_all[count] + ".csv"
    if csv_name not in filenames:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        tqtongji1 = soup.find("div",{"class":"tqtongji1"})
        # print(tqtongji1)
        ul_all = tqtongji1.find_all("ul")
        # print(ul_all)
        month_url = []
        # 获取城市对应url下的全部月份url
        for i in ul_all:
            li_all = i.find_all("li")
            for j in li_all:
                # print(j.a.get("href"))
                month_url.append(j.a.get("href"))
        data_all=[]
        # print(month_url)
        for each_url in month_url:
            response = requests.get(each_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(response.text)
            tqtongji2=soup.find("div",{"class":"tqtongji2"})
            ul_all=tqtongji2.find_all("ul")
            for i in ul_all:
                li_all=i.find_all("li")
                data=[]
                flag = True
                for j in li_all:
                    data.append(j.text)
                data_all.append(data)
        weather=pd.DataFrame(data_all)
        weather.columns=["日期","最高气温","最低气温","天气","风向","风力"]
        weather.drop([0],inplace=True)
        # print(city_all[count]+".csv")
        weather.to_csv('./delete_data/'+city_all[count] + ".csv", encoding="utf_8_sig")
        print(csv_name)
    else:
        print(csv_name)
    count += 1
    end_time = time.time()
    print(end_time - start_time)
    

#weather=pd.DataFrame(data_all)
#weather.columns=["日期","最高气温","最低气温","天气","风向","风力"]
#weather.drop([0],inplace=True)
#weather.to_csv("qingdao201603.csv",encoding="utf_8_sig")

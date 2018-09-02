
import urllib.request as request
import json #處理JSON資料格式(javascrip object notation)
with request.urlopen("https://opendata.epa.gov.tw/api/v1/RainTenMin?$skip=0&$top=1000&$format=json") as response:#response=request.urlopen()
   #data=response.read().decode("utf-8")
   data=json.load(response)

# keyword=list(map(str, input('請輸搜尋地區名稱，間隔請以","隔開：').split(',')))
keyword=input("搜尋地區名稱：")
#資料存入rain_data.txt
list=data
with open("rain_data.txt","w",encoding="utf-8") as file:
    n = 0
    for Rain in list:
        if Rain["County"] == keyword:
            file.write(str(Rain["Rainfall24hr"])+"\n") 
            n = n+1
        else:
            continue
    
    if n > 0:
        print("已存入資訊!")
             
    else:  
        print('查無此縣市!')

# 讀取檔案加總
total=0
with open('rain_data.txt', 'r') as inp, open('output.txt', 'w') as outp:
   for line in inp:
       try:
           num = float(line)
           total += num
           outp.write(line)
       except ValueError:
           print(line)
print(total)

analyzeData={
    keyword:total
}
print(analyzeData)


import plotly.plotly as py
import plotly.graph_objs as go

labels=[]
values=[]


for name in analyzeData:
    labels.append(name)
    values.append(analyzeData[name])
print(labels)
print(values)

data=[go.Bar(
            x=labels,
            y=values
    )]

#畫圖
py.plot(data,filename="mychart",auto_open=True)



# def analyzeData():

#直接print input的對應值
# list=data
# for Rain in list:
#     if keyword in Rain["County"]:
#         print (Rain["Unit"]+Rain["Rainfall24hr"])

#嘗試加總Rainfall24hr
# list=data
# total=0
# for Rain in list:
#     if keyword in Rain["County"]:
#         for Rainfall24hr in list:
#             try:
#                 num = float(Rainfall24hr)
#                 total += num
#                 list.write(Rainfall24hr)
#             except ValueError:
#                 print('{} is not a number!'.format(Rainfall24hr))

# with open('rain_data.txt', 'r') as inp, open('output.txt', 'w') as outp:
#    for line in inp:
#        try:
#            num = float(line)
#            total += num
#            outp.write(line)
#        except ValueError:
#            print('{} is not a number!'.format(line))

# print('Total of all numbers: {}'.format(total))




#讀取檔案
# with open("rain_data.txt","r",encoding="utf-8") as file:
#     data=file.read()#讀取所有資料
#     print(data)



#逐行讀取
# with open("data.txt","r",encoding="utf-8") as file:
#     for line in file: #line為變數
#         print(line,end="")#使結尾為無空白





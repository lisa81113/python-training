#作業：
#1.特定捷運站附近的景點
#2.將對應到的景點資訊，儲存在檔案中

import urllib.request as request
import json #處理JSON資料格式(javascrip object notation)
src="http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5"
with request.urlopen(src) as response:#response=request.urlopen()
   data=json.load(response)

keyword=input("搜尋捷運站名稱：")

#將捷運站表列出來
mlist=data["result"]["results"]
with open("mrt_data.txt","w",encoding="utf-8") as file:
    n = 0
    for mrt in mlist:
        if mrt["MRT"] == keyword:
            file.write(str(mrt["stitle"])+"\n") 
            n = n+1
        else:
            continue
    
    if n > 0:
        print("已存入景點!")
             
    else:  
        print('查無此捷運站唷!')
        
   
    
        
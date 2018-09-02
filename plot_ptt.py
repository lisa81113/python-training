import urllib.request as request
import ssl
import bs4

def getData(src):
    context=ssl._create_unverified_context()
    req=request.Request(src,headers={
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    })
    with request.urlopen(req,context=context) as response:
        data=response.read().decode("utf-8")
    #print(data)
    root=bs4.BeautifulSoup(data,"html.parser")
    #擷取標題的資料
    titles=root.find_all("div","title")
    titleList=[]
    for title in titles:
        if title.a!=None:
            titleList.append(title.a.string)
    #擷取下一頁的網址
    nextLink=root.find("a",string="‹ 上頁")
    next=nextLink["href"]
    return{
        "titles":titleList,
        "next":next
    }
    
#建立分析資料的函式
cities={
    "台北":0,
    "新北":0,
    "桃園":0,
    "台中":0,
    "台南":0,
    "高雄":0
}
def analyzeData(titles):
    for title in titles:
        for name in cities:
            if name in title:
                cities[name]+=1
#使用getData函式
host="https://www.ptt.cc"
src=host+"/bbs/home-sale/index.html"
for i in range(1):
    data=getData(src)
    analyzeData(data["titles"])
    src=host+data["next"]

#用圓餅圖畫出來
print(cities)
import plotly.plotly as py
import plotly.graph_objs as go

labels=[]
values=[]
#將資料拆開
for name in cities:
    labels.append(name)
    values.append(cities[name])
print(labels)
print(values)

data=go.Pie(
    labels=labels,
    values=values
)

#畫圖
py.plot([data],filename="mychart",auto_open=True)
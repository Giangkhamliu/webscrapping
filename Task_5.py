import requests,json
from bs4 import BeautifulSoup
url_list=[]
with open('Top_250_movies.json','r') as f:
    a=json.load(f)
for i in a:
    url_list.append(i['link'])
list=[]
for j in url_list:
    rel=requests.get(j)
    soup=BeautifulSoup(rel.text,"html.parser")
    con=soup.find('script',type='application/ld+json').text
    h=json.loads(con)
    dic={}
    for k in h:
        dic['name']=h['name']
        dic['director']=h['director'][0]['name']
        dic['image']=h['image']
        dic['description']=h['description']
        dic['language']=h['review']['inLanguage']
        dic['genre']=h['genre']
        dic['Runtime']=h['duration']
        dic['country']='india'
    list.append(dic)
with open('Task_5.json','w') as file:
    json.dump(list,file,indent=8)
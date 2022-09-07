import json
with open('Task_5.json','r') as f:
    a=json.load(f)
d={}
dic={}
i=0
eng=0
h=0
t=0
te=0
while i<len(a):
    if a[i]['director']=="Madhavan":
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            h=h+1
            dic['Hindi']=h
            d['']=dic
        if  a[i]['language']=='Tamil':
            t=t+1
            dic['Tamil']=t
        if  a[i]['language']=='Telugu':
            te=te+1
            dic['Telugu']=t
    if a[i]['director']=='Sundar C.':
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            h=h+1
            dic['Hindi']=h
            d['']=dic
        if  a[i]['language']=='Tamil':
            t=t+1
            dic['Tamil']=t
        if  a[i]['language']=='Telugu':
            te=te+1
            dic['Telugu']=t
    if a[i]['director']=='Mani Ratnam':
        if a[i]['language']=='English':
            eng=eng+1
            dic['english']=eng
        if  a[i]['language']=='Hindi':
            h=h+1
            dic['Hindi']=h
            d['']=dic
        if  a[i]['language']=='Tamil':
            t=t+1
            dic['Tamil']=t
        if  a[i]['language']=='Telugu':
            te=te+1
            dic['Telugu']=t

    i+=1
    d['Hrishikesh Mukherjee']=dic
    d['Sundar C.']=dic
    d['Mani Ratnam']=dic

with open('imdb 10_task.json','w')as f:
    json.dump(d,f,indent=6)
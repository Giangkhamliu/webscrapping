import json
with open ('Task_5.json','r') as f:
    a=json.load(f)
dic={}
i=0
count=0
while  i<len(a):
    if a[i]['language']=='English':
        count=count+1
        dic['English']=count
    i=i+1
with open ("Task_6.json","w") as f:
    json.dump(dic,f,indent=4 )
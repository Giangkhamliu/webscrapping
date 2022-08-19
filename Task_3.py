import json
with open ("Task2.json") as file:
    new=json.load(file)
def group_by_decade(new):
    y=1950
    dic={}
    for i in range(y,2022,10):
        movies_list=[]
        for j in new:
            if y<int(j) and int(j)<(y+10):
                movies_list.append(new[j])
        dic[y]=movies_list  
        y+=10
    with open ("Task3.json","w") as f1:
        json.dump(dic,f1,indent=4)
    print(dic)
group_by_decade(new)
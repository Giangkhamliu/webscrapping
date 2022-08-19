import json
new=open("Top_250_movies.json","r")
task=json.load(new)
# print(task)
dic={}
for i in task:
    movie_list=[]
    year=i["year"]
    if year not in dic:
        for j in task:
            if year==j["year"]:
                movie_list.append(j)
        dic[year]=movie_list
    print(dic)
with open("Task2.json","w") as f:
        json.dump(dic,f,indent=8,sort_keys=True)

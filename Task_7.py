import json
with open("Task_5.json","r") as f:
    a=json.load(f)
Director_count={}
i=0
while i <len(a):
    if a[i]["director"] in Director_count:
        Director_count[a[i]["director"]]+=1
    else:
        Director_count[a[i]["director"]]=1
    i=i+1
    # print(Director_count)
with open ("Task_7.json","w") as k:
    json.dump(Director_count,k,indent=2)

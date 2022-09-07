import json
with open("Task_5.json","r") as f:
    a=json.load(f)
analyze_language_and_directors={}
i=0
while  i<len(a):
    j=0
    dic={}
    while j<len(a):
        if a[j]["director"]in dic:
            dic[a[j]["language"]]+=1
        else:
            dic[a[j]["language"]]=1
        analyze_language_and_directors[a[j]["director"]]=dic
        j+=1
    i+=1
    print(analyze_language_and_directors)
with open ("Task_10.json","w") as k:
    json.dump(analyze_language_and_directors,k,indent=2)







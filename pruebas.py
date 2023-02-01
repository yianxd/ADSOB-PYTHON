dic={
    "a":{
        "b":{
            "a":{
                "v":{
                    "a":1
                }
            }
        },
        "b1":{
            "v":{
                "e":{
                    "a":2
                }
            }
        }
    }
}


a,a2=0,0
for i in dic["a"]:
    for k in dic["a"][i]:
        for l in dic["a"][i][k]:
            for j in dic["a"][i][k][l].values():
                print(l)
                a=j
                if a2<a:
                 a2=j
                else:
                 a=a2
print(a2)
print(a)
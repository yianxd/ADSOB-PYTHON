
num="100"
for i in range(100,999,1):
    f1=int(num[0:1])
    f2=int(num[1:2])
    f3=int(num[2:3])
    i=(f1**3)+(f2**3)+(f3**3)
    num=int(num)
    num+=1
    num=str(num)
    #print(i)
    if i==num:
        print(i)
    else:
        print("no existe")





""""
num=(input())
f1=int(num[0:1])
f2=int(num[1:2])
f3=int(num[2:3])

if int(num)>=100 and int(num)<=999:
    for i in range(100,1000,1):
        i=f1**3+f2**3+f3**3
print(i)
"""
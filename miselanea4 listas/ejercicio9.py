import random 
a=[]
media=0
for i in range(random.randint(10,25)):
    a.append(random.randrange(100))
if len(a)%2==0: 
    for i in range(len(a)):
        if len(a)>2:
         del a[0]
         del a[-1]
         media=(a[0]+a[1])/2
else:
    for i in range(len(a)):
        if len(a)>1:
         del a[0]
         del a[-1]
         media=[a[0]]
print(media)
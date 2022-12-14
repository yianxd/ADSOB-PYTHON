num=int(input("Ingrese la cantidad de veces que quiere que se repita el ciclo: "))
a=[0,1]
#a[1]+a[2]=a[3]
for i in range(num):
    a.append(a[-1]+a[-2])
print(a)

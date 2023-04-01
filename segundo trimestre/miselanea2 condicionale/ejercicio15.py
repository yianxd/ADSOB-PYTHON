año=int(input("Ingrese un año: "))
A=año%19
b=año%4
c=año%7
d=(19*A+24)%30
e=(2*b+4*d+5)%7
n=(22+d+e)

if n<=31:
    print("el dia es en marzo ",n)
else:
    n-=31 
    print("el dia corresponde a abril ",n)
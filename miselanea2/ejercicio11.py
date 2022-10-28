num=int(input("Escriba un valor entero: "))
b_1=0
b_2=0
b_5=0
b_10=0
b_50=0
if num>=50000:
    if num%50000==0:
        b_50=num/50000
        print("hay",b_50,"de 50000")
    
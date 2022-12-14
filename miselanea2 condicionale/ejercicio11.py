num=int(input("Escriba un valor entero: "))
b_1=0
b_2=0
b_5=0
b_10=0
b_20=0
b_50=0
if num>=50000:
    b_50=num//50000
    num-=b_50*50000
if num>=20000:
    b_20=num//20000
    num-=b_20*20000
if num>=10000:
    b_10=num//10000
    num-=b_10*10000
if num>=5000:
    b_5=num//5000
    num-=b_5*5000
if num>=2000:
    b_2=num//2000
    num-=b_2*2000
if num>=1000:
    b_1=num//1000
    num-=b_1*1000

print("Hay un total de\n",b_50,"billetes de cienta\n",b_20,"billetes de viente\n",b_10,"billtes de diez",b_5,"billetes de cinco\n",b_2,"billetes de dos\n",b_1,"billetes de mil")
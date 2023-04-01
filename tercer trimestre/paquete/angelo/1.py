
def area(area):
    i=area*area
    return("el resultado de un cuadrado es:",i)
area=int(input("introduce el area \nR:"))
print(numero(area))    


def perimetro(perimetro):
    a=perimetro*3
    return("este es el perimetro:",a)

def numero(num):
    c=[] 
    tam=len(c)
    media=0
    for i  in range(1,num):
        if i %2==0:
            media.append(i)
            media =  num // tam
    return(c)

    
    

            
        
  

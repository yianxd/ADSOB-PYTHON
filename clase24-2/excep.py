try: #bloque try:)
    #print(1/1)) comentario xd
    raise SyntaxError #simula un SyntaxError
except SyntaxError: #si se da "SyntaxError" para algo
    print('Cierra el parentesis') #pasa estoxd
    
    
values = (1, 0) #es una tupla 
#x,y=19,30 determinador dos variables en una sola linea
#print(divmod(10,3)) divmod divide el primer numero por el segundo y retorna la cantidad de veces que esta el segundo número en el primero y el reducio
try: #bloque try:)
    q, r = divmod(*values) #guarda en las variables q y r el divmod de la tupla values
    #print('q=',q) #contatenar un str con un valor numero
    print(f'q={q}') #es una plantilla literal que permite escribir str con un valor numero
    print(f'r={r}') #lo mismo de arriba
except (ZeroDivisionError, TypeError) as e: #en este except se guardar 2 errores en una tupla con el fin de escribir tantos bloques except y el as le dara un "apodo" con el cual llamarle
    print(type(e), e) #imprime por pantalla el valor de e
    

def try_syntax(numerator, denominator): #determina una funcion de nombre con el nombre dado con los parametros de numetator y denominator
    try: #inicio de bloque try
        print(f'In the try block: {numerator}/{denominator}') #imprime por pantalla una plantilla literal con el mismo dado y la variable numerator y denominator 
        result = numerator / denominator #guarda el resultado la division numerator y denominator
    except ZeroDivisionError as zde: #bloque expect que se da en el caso de ser ZeroDivisonError y se le dara el "apodo" de zde
        print(zde) #impreme el error
    else: #en caso no entrar en el bloque except entra  por aqui
        print('The result is:', result) #imprime por pantalla el mensaje entre comillas y la variable result
        return result #retorna la variable result al fanlizar el proceso
    finally: #finally siempre se ejecutara
        print('Exiting') #imprime por pantalla el mensaje entre comillas
        #return "Fallo por zero" 
#print(try_syntax(12, 4)) #envia parametros a la funcion
print(try_syntax(11, 0)) #envia paramatros a la funcion para entre a except

def edad(): #inicio de la funcion
    try:  #inicio del bloque try
        tuedad=int(input("introduce tu edad")) #guarda en una variable lo que se introduzca por teclado 
        print(f'tu edad es  {tuedad}') #imprime por pantalla una plantilla literal con la variable y el texto dado
        #print('Tu edad es ',tuedad) #imprime por pantalla concatenando un string y una variable tipo int
    except ValueError as e:    #en caso que aparezca un ValueError entrara aqui y se le dara el apodo de e
        print(e) #imprime el error
        print("La edad debe ser un valor numerico...") #mensaje por pantalla
        edad() #vuelve a entrar en la funcion creacion un bucle
    else: #se dara en caso que no entre al except
        print('Viene por el else') #

edad() #llamado de la funcion

    




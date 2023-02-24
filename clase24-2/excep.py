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
    except ZeroDivisionError as zde: #bloque expect que se da en el caso de ser ZeroDivisonError y se le dara el "apado" de zde
        print(zde) #impreme el error
    else: #en caso no entrar en el bloque except entra  por aqui
        print('The result is:', result) #imprime por pantalla el mensaje entre comillas y la variable result
        return result #retorna la variable result al fanlizar el proceso
    finally: #finally siempre se ejecutara
        print('Exiting') #imprime por pantalla el mensaje entre comillas
        #return "Fallo por zero" 
#print(try_syntax(12, 4)) #
print(try_syntax(11, 0))

    




#1 Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def buscar(cadena):
    abc="aAbBcCdDeEfFgGhHiIjJkKlLmMñÑnNsStTuUvVwWxXyYzZ"
    cont=0
    cadena2=""
    for i in cadena:
        if i not in cadena2:
            cadena2+=i 
    for i in cadena2:

        for j in abc:
                if i==j:
                    cont+=1
    return cont

#print(buscar("juuuuuan"))

#2 Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto
def codigo(cadena=""):
    cadena=input()
    suma=0
    for i in cadena:
        suma+=ord(i)
    return suma

#print(codigo())

#3 cuantas veces se repite un caracter dado
def contar(cadena="",caracter=""):
    cadena,caracter=input(),input()
    return cadena.count(caracter)
    
#print(contar())
#4 Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def mm(cadena=""):
    lista=[]
    cadena=input()
    lista.append(cadena.upper())
    lista.append(cadena.lower())
    lista.append(cadena.title())
    
    return lista

#print(mm())
#5 Determinar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
"""def t_palabra(cadena):
    a="áÁéÉíÍóÓúÚ"
    a="ácasa"
    a2="áÁéÉíÍóÓúÚ"
    palabra=""

    for i in a:
        for j in a2:
            #a3=a[-5:-1]
            if i==j or  a[-1]=="n" or a[-1]=="s":
                palabra="aguda"
            elif      a[-1]!="n" or a[-1]!="s":
                palabra="grave"
print(palabra)


slice=a[-5:-1]
print(slice)
"""
#6.Determinar en que tiempo esta conjugado un verbo



#7.De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def cad(cadena):
    vocales='aeiouAEIOU'
    consonantes='bcdfghjklmnñopqrstvwxyzBCDFGHJKLMNÑOPQRSTUVWXYZ'
    tildes='áéíóúÁÉÍÓÚ'
    v=0
    c=0
    t=0
    e=0
    for i in cadena:
        if i in vocales:
            v+=1
        elif i in tildes:
            t+=1
        elif i in consonantes:
            c+=1
        else:
            e+=1
    print("vocales: ",v,"consonantes: ",c,"tildes: ",t,"caracter especial: ",e)

#cad("cadená1")
#8.  Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def cifrado(cadena):
    cadena.lower
    lis=[]
    a=["a","e","i","o","u"]
    n_cadena=""
    for i in cadena:
        if i in a:
            if i=="a":
                i="z"
                lis.append(i)
            if i=="e":
                i="w"
                lis.append(i)
            if i=="i":
                i="s"
                lis.append(i)
            if i=="o":
                i="j"
                lis.append(i)
            if i=="u":
                i="f"
                lis.append(i)
        else:
            lis.append(i)
    print("palabra sin cifrado: ",cadena)
    print("palabra con cifrado ",n_cadena.join(lis)) 

cifrado("no se que escribir")
#9. Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última
def subc(cadena):
    a=0
    for i in cadena:
        a+=1
        print(cadena[0:a]) 


subc("cadena")
import csv #importa el modulo csv que permite trabajar con archivos .csv
header=['Fruit','Price'] #crea una lista con el nombre header que funcionara como un encabezado
rows=[['Apple',1200], #Desde la linea 3 hasta la linea 8  se crea una lista
      ['Berry',2000], # que contiene mas listas con el nombre de una fruta en el indice 0
      ['Lemon',1000], #y en el indice 1 el precio
      ['Melon',3000], #
      ['Grapes',4000],# 
      ['Pear',2000]]  #

with open ('archivos/example.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
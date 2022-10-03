# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from itertools import count
##from termios import VSTART


def ej3():
    print('Ejercicio de archivos CSV 1º')

    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    stock_csv = open('stock.csv')
    stock =  list(csv.DictReader(stock_csv))
    stock_csv.close()
    sumatoria = 0 

    for articulo in stock:
       sumatoria += int(articulo['tornillos'])
       
    print('el total de tornillos es :' , sumatoria)


    


def ej4():
    print('Ejercicios con archivos CSV 2º')
     
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = open('propiedades.csv' , 'r')
    dptos = list(csv.DictReader(archivo))
    archivo.close()
    suma_2amb = 0
    suma_3amb = 0
    cant_dptos = len(dptos) #para convertir la lista y su largo.

    for departamento in range(cant_dptos):
         row = dptos[departamento]
         try :
            cant_amb = int(row.get('ambientes'))
            if  cant_amb ==2:
                   suma_2amb += 1
            if cant_amb == 3:
                  suma_3amb += 1 
         except:
            None
    print('La cantidad de departamentos de 2 ambientes es:' , suma_2amb , 
    'y la de 3 ambientes es de :' , suma_3amb)

    
   
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()


"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def topVoted(catalog, parameter):
    top_voted = []
    for i in range(len(catalog)):
        if float(catalog[i]['vote_average']) >= parameter:
            top_voted.append({catalog[i]['\ufeffid']:float(catalog[i]['vote_average'])})
        i += 1
    return top_voted

def moviesByDirector(directorname, catalog):
    movies = []
    for i in range(len(catalog)):
        if catalog[i]['director_name'] == directorname:
            movies.append(catalog[i]['id'])
    return movies

def loadCSVFile(file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    lst = []
    del lst[:]
    print("Cargando archivo ....")
    """t1_start = process_time() #tiempo inicial"""
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    """t1_stop = process_time() #tiempo final"""
    """print("Tiempo de ejecución ",t1_stop-t1_start," segundos")"""
    return lst
    

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar buenas peliculas segun director")
    print("0- Salir")

def countElementsFilteredByColumn(criteria,column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            print(element)
            print(element[column])
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(nombredirector,direc1,direc2,id): 
    t1_start = process_time() #tiempo inicial 
    movies_casting = loadCSVFile(direc1)
    movies_details = loadCSVFile(direc2)
    movies = moviesByDirector(nombredirector,movies_casting)
    iguales = []
    for i in range(len(movies_details)):
        for x in movies:
            if movies_details[i][id] == x:
                if float(movies_details[i]['vote_average']) >= 6.0:
                    iguales.append(movies_details[i]['vote_average'])
    cantidad = len(iguales)
    average = 0.0
    for i in iguales:
        average += float(i)
    average = average/cantidad
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (cantidad,average)

def menuReq1():
    print('1. Probar con archivos grandes')
    print('2. Probar con archivos pequeños')
    opcion = input('Digite su opcion: ')
    return opcion

def opcionesReq1():
    opcion = menuReq1()
    continuar = True
    while continuar == True:
        if opcion == '1':
            direc1 = 'Data/themoviesdb/AllMoviesCastingRaw.csv'
            direc2 = 'Data/themoviesdb/AllMoviesDetailsCleaned.csv'
            id = '\ufeffid'
            continuar = False 
        elif opcion == '2':
            direc1 = 'Data/themoviesdb/MoviesCastingRaw-small.csv'
            direc2 = 'Data/themoviesdb/SmallMoviesDetailsCleaned.csv'
            id = 'id'
            continuar = False
        else:
            opcion = input('Opcion errada, digite nuevamente su opcion: ')
    return (direc1, direc2, id)


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = [] #instanciar una lista vacia
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                file = input('Digite la direccion del archivo a cargar: ')
                lista = loadCSVFile(file,lista) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                column = input('Ingrese la columna en la que quiere buscar: ')
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria,column, lista) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el nombre del director\n')
                datos = opcionesReq1()
                counter=countElementsByCriteria(criteria, datos[0],datos[1], datos[2])
                print("Coinciden ",counter[0]," elementos con el director: '", criteria ,"' con un promedio de votacion de", round(counter[1],2))
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()

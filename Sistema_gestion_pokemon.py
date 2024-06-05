import os
import msvcrt
import csv

#Cargar los pokemon del csv
pokemones = ""
with open('pokemon_primera_generacion.csv', newline='', encoding='utf-8') as a:
    datos = csv.reader(a, delimiter=",")
    pokemones = list(datos)
#Creamos coleccion para el cinturon
cinturon = []
#Comenzamos sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")
    print("""
    Sistema de gestion cinturon pokémon
    -----------------------------------
    1) Mostrar
    2) Buscar pokemon
    3) Agregar al cinturon
    4) Mostrar el cinturon
    5) Quitar del cinturon
    0) Salir""")
    opcion = input("Seleccione : ")

    if opcion=="0":
        break
    elif opcion=="1":
        print("Listado de pokemones")
        for p in pokemones:
            print(f"{p[0]}\t{p[1]}\t{p[3]}\t{p[4]}")
    elif opcion=="2":
        print("Buscar pokemon")
    elif opcion=="3":
        print("Agregar cinturon")
    elif opcion=="4":
        print("Mostrar cinturon")
    elif opcion=="5":
        print("Quitar del cinturon")
    else:
        print("Opcion no valida")
   

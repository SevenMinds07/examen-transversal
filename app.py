from funciones import *

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "aura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
pagos = []


while True:
    print("Bienvenido a R.R.H.H de SevenEnterprise")
    print("1- Asignar sueldo a los empleados")
    print("2- Clasificar sueldos")
    print("3- Ver estadísticas")
    print("4- Reporte de sueldos")
    print("5- Salir del programa")
    opcion=int(input("Ingrese la opción que desea realizar: "))

    if opcion==1:
        asignar_sueldo(trabajadores, pagos)
    elif opcion==2:
        clasificar_sueldos(trabajadores, pagos)
    elif opcion==3:
        print("Holiwi")
    elif opcion==4:
        print("chao nomas")
    elif opcion==5:
        cerrar_programa()
        break
    else:
        print("Opción invalida, intente de nuevo")
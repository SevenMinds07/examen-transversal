import random
import csv
import math

def asignar_sueldo(trabajadores, pagos):
    for x in trabajadores:
        sueldo=int(random.uniform(300000, 2500000))
        pagos.append(sueldo)
        
def clasificar_sueldos(trabajadores, pagos):
    suelsum=sum(pagos[x] for x in pagos)
    print(f"La suma de los suelos es: {suelsum}")

def ver_estats(trabajadores, pagos):
    print()
        
def reporte_sueldos(trabajadores, pagos, filename='guardado.cxv'):
    if pagos:

        keys= pagos[0].keys()
        key= trabajadores[0]
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldname=keys)
            dict_writer.writeheader()
            dict_writer.writerows(pagos)
            print(f"Reporte guardado en {filename}")
    else:
        print("No hay nada para guardar.")

def cerrar_programa():
    print("Cerrando programa...")
    print("Desarrollado por Diego Muñoz B.")
    print("21.591.413-5")
            
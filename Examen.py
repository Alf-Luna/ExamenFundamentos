import random
import statistics
import csv
def GenerarSueldo():
    num = random.randrange(300000, 2500000)
    return num

def SueldosClasificados(_trabajadores, _sueldos):
    percentil1 = {}
    for indx in range(len(_sueldos)):
        if _sueldos[indx] < 800000:
            percentil1[_trabajadores[indx]] = _sueldos[indx]
    print(f"Sueldos menores a 800000 TOTAL: {len(percentil1.keys())}")
    for llave in percentil1.keys():
        print(f"{llave}     ${percentil1[llave]}")
    print("")

    percentil2 = {}
    for indx in range(len(_sueldos)):
        if 800000 <= _sueldos[indx] < 2000000:
            percentil2[_trabajadores[indx]] = _sueldos[indx]
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(percentil2.keys())}")
    for llave in percentil2.keys():
        print(f"{llave}     ${percentil2[llave]}")
    print("")

    percentil3 = {}
    for indx in range(len(_sueldos)):
        if _sueldos[indx] > 2000000:
            percentil3[_trabajadores[indx]] = _sueldos[indx]
    print(f"Sueldos mayores a $2.000.000 TOTAL: {len(percentil3.keys())}")
    for llave in percentil3.keys():
        print(f"{llave}     ${percentil3[llave]}")

def Estadisticas(_trabajadores, _sueldos):
    print("Estadistícas:")
    sueldoAlto = 0
    trabajadorSueldoAlto = ""
    for indx in range(len(_sueldos)):
        if _sueldos[indx] > sueldoAlto:
            sueldoAlto = _sueldos[indx]
            trabajadorSueldoAlto = _trabajadores[indx]
    print("Sueldo más alto:", trabajadorSueldoAlto, "$", sueldoAlto)

    sueldoBajo = 2500001
    trabajadorSueldoBajo = ""
    for indx in range(len(_sueldos)):
        if _sueldos[indx] < sueldoAlto:
            sueldoAlto = _sueldos[indx]
            trabajadorSueldoAlto = _trabajadores[indx]
    print("Sueldo más bajo:", trabajadorSueldoAlto, "$", sueldoAlto)

    promedioSueldos = 0
    for sueldo in _sueldos:
        promedioSueldos += sueldo
    promedioSueldos /= 10
    print("Promedio de sueldos (redondeado): $", promedioSueldos.__round__())

    print("Media geométrica de sueldos: (redondeada): $", statistics.geometric_mean(_sueldos).__round__())

def ReporteSueldos(_trabajadores, _sueldos):
    headers = ["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"]
    print(f"{headers[0]}    {headers[1]}    {headers[2]}    {headers[3]}    {headers[4]}")
    with open("ReporteSueldos.csv", "w", encoding="utf-8", newline="") as archivo:
        archivo = csv.writer(archivo)
        archivo.writerow(headers)
        for indx in range(len(_sueldos)):
            nombre = _trabajadores[indx]
            sueldo = _sueldos[indx]
            descuentoSalud = (sueldo * 0.07).__round__()
            descuentoAFP = (sueldo * 0.12).__round__()
            sueldoLiquido = (sueldo - descuentoSalud - descuentoAFP).__round__()
            archivo.writerow([nombre, sueldo, descuentoSalud, descuentoAFP, sueldoLiquido])
            print(f"{nombre}   ${sueldo}   ${descuentoSalud}   ${descuentoAFP}   ${sueldoLiquido}")

def Salir():
    print("Finalizando programa...")
    print("Desarrollado por Alfonso Luna Aravena")
    print("RUT 20.075.222-8")

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []
sueldosGenerados = False

print("Bienvenido al prototipo de aplicación para analizar datos del personal.")
while True:
    print("Las operaciones disponibles son:")
    print("1. Generar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    selc = input("Ingrese la operación que desea realizar: ")
    match selc:
        case "1":
            sueldos = [GenerarSueldo() for trabajador in trabajadores]
            sueldosGenerados = True
            print("Sueldos generados.")
    
        case "2":
            if sueldosGenerados:
                SueldosClasificados(trabajadores, sueldos)
            else:
                print("Para realizar operaciones por favor genere los sueldos primero.")
    
        case "3":
            if sueldosGenerados:
                Estadisticas(trabajadores, sueldos)
            else:
                print("Para realizar operaciones por favor genere los sueldos primero.")

        case "4":
          if sueldosGenerados:
            ReporteSueldos(trabajadores, sueldos)
          else:
                print("Para realizar operaciones por favor genere los sueldos primero.")
    
        case "5":
            Salir()
            break

        case _:
            print(f"No se encontrado la opción '{selc}'")
    print("")
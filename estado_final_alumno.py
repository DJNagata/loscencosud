import csv
#******************[FUNCION CALCULO DE NOTAS]*******************************
def presentacion_examen(p1,p2,p3):
    notapresentacion = round(p1 * 0.3 + p2 * 0.35 + p3 * 0.35)
    return notapresentacion

#******************[FUNCION CALCULO DE ASISTENCIA]**************************
def calcular_asistencia_y_estado(lista):
    asistencia_presentes = 0
    estado = ""
    for i in range (4,11):
        asistencia_presentes = asistencia_presentes + int(row[i])
    porcentaje_asistencia = round((asistencia_presentes / 7) * 100)
    print("Dias asistidos: ", asistencia_presentes,"de 7 \ Porcentaje de asistencia: ", porcentaje_asistencia,"%")    
    if porcentaje_asistencia >= 65:
        estado = "Aprobada"
    else:
        estado = "Desaprobada"
    #print(lista)
    return estado

#******************[FUNCION CREACION DE ARCHIVO]****************************
def generar_archivo(lista_final):
    with open('ista.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        cabecera = ["nombre","p1","p2","p3","a1","a2","a3","a4","a5","a6","a7"]
        escritor_csv.writerow(cabecera)
        for row in lista_final:     
            escritor_csv.writerow(row)
    return
    
#*****************************[MAIN]****************************************
cantidad_alumnos = 0
total_notas_curso = 0
with open('ista.csv','r', newline='') as csvfile:
    lector_csv = csv.reader(csvfile)
    next(lector_csv)
    temporal = []
    for row in lector_csv:
        cantidad_alumnos = cantidad_alumnos + 1
        nombre = row[0]
        nota1 = int(row[1])
        nota2 = int(row[2])
        nota3 = int(row[3])
        promedio_alumno = presentacion_examen(nota1,nota2,nota3)
        total_notas_curso = total_notas_curso + promedio_alumno
        estado = calcular_asistencia_y_estado(row)
        print("Asistencia: ",estado, "\nNombre: ",nombre,"\nNota 1",nota1,"\nNota 2",nota2,"\nNota 3",nota3,"\nPromedio Alumno: ",promedio_alumno,"\n***************************************")
        row.append(estado)
        row.append(promedio_alumno)
        temporal.append(row)
        #print(temporal)
        
    #print(temporal)    
    #next(lector_csv)
    #for row in lector_csv:
        #print(lector_csv[row])
generar_archivo(temporal)
print("-----------------------------","\nEl promedio del curso es: ", round(total_notas_curso/cantidad_alumnos),"\n------------------------------")

#for row in lector_csv:
    #print(temporal)
        



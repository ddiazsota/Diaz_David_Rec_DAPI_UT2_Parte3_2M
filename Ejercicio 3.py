def calculate_grade(Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud):
    """Esta función consiste en que a partir de los datos de proccess class 
    calcule la nota media de los alumnos/as y función recibirá las notas de todos 
    los apartados evaluados de cada alumno/a y devolverá unanota final y un valor Verdadero/Falso
    en función de si ha aprobado o suspendido.
    NotaFinal = (Practica01 + Practica02 +Practica03)/3 * 0,3 +
    max(Examen; Recuperacion)* 0,6 + Actitud * 0,1
    Parámetros:
        -Fichero class.csv
        -Seis float con las notas de cada alumno:
         Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud
        Salida:
            -Asigatura superada o no
    """
    Examen2 = [Examen, Recuperacion]
    total_practicas = Practica01 + Practica02 + Practica03
    NotaFinal = total_practicas/3 * 0.3 + max(Examen2)* 0.6 + Actitud * 0.1
    NotaFinal = round(NotaFinal, 2)
    if NotaFinal >= 5:
        return NotaFinal,True
    else:
        return NotaFinal,False
print(calculate_grade(2.3,6.5,2.7,2,6,8))
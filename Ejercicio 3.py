def calculate_grade(Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud):
    Examen2 = [Examen, Recuperacion]
    total_practicas = Practica01 + Practica02 + Practica03
    NotaFinal = total_practicas/3 * 0.3 + max(Examen2)* 0.6 + Actitud * 0.1
    NotaFinal = round(NotaFinal, 2)
    if NotaFinal >= 5:
        return NotaFinal,True
    else:
        return NotaFinal,False
print(calculate_grade(2.3,6.5,2.7,2,6,8))
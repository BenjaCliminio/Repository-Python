#a) Diferencia en porcentaje entre el curso actual y: -El mas rapido de otros cursos, -El mas lento de otros cursos, -El promedio de los cursos
curso_actual = 1.5

curso_mas_rapido = 2.5

curso_mas_lento = 7

curso_promedio = 4

Diferencia_con_mas_rapido = 100 - (curso_actual / curso_mas_rapido) *100
Diferencia_con_mas_lento = 100 - (curso_actual / curso_mas_lento) *100
Diferencia_con_promedio = 100 - (curso_actual / curso_promedio) *100

print("------------------")
print(f"La diferencia de porcentaje entre el curso actual y el mas rapido es de: {Diferencia_con_mas_rapido}%")
print(f"La diferencia de porcentaje entre el curso actual y el mas lento es de: {Diferencia_con_mas_lento}%")
print(f"La diferencia de porcentaje entre el curso actual y el mas promedio es de: {Diferencia_con_promedio}%")
print("------------------")

#b) Porcentaje de marterial inservible que se reduce en: -El promedio de los cursos, El curso actual
crudo_promedio = 5
crudo_principal = 3.5



tiempo_vacio_promedio = 100 - (curso_promedio *1000 // crudo_promedio  / 10) 
tiempo_vacio_principal = 100 - (curso_actual *1000 // crudo_principal  / 10) 


print(f"El porcentaje de material inservible en un curso promedio es de: {tiempo_vacio_promedio}%")
print(f"El porcentaje de material inservible en el curso principal es de: {tiempo_vacio_principal}%")
print("------------------")


#c) Ver 10 horas de este curso a cuantas equivale de otros cursos, y al reves?
diferencia_de_horas_curso_principal = round((curso_promedio / curso_actual),1)
diferencia_de_horas_curso_promedio = round((curso_actual / curso_promedio),1)


print(f"Ver 10 horas de este curso equivale a ver: {diferencia_de_horas_curso_principal} horas de otros cursos")
print(f"Ver 10 horas de un curso promedio equivale a ver: {diferencia_de_horas_curso_promedio} horas de este curso")
print("------------------")
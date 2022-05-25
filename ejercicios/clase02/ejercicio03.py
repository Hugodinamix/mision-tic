print("-------¿Cuántas vueltas dará un Fidget Spinner?-------")
print("Sabemos que un Fidget Spinner da 147 vueltas por minuto \n¿Cuántas vueltas dará en 640 segundos? \nPara este ejercicio se desprecia el rozamiento con el aire. \n")

# solución
vueltas_por_minuto = input("Introduce un número de vueltas por minuto: ")
minutos_a_segundo = 60
vueltas_por_tiempo_especifico = input("\n¿cuantos segundos necesita aplicar?: ")
vueltas_finales = ((int(vueltas_por_minuto)*int(vueltas_por_tiempo_especifico))/minutos_a_segundo)
print(f"\nEl Fidget Spiner da {vueltas_finales} en {vueltas_por_tiempo_especifico} segundos.")

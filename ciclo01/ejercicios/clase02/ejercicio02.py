print("-------¿CUÁNTO COSTARÁ EL TELÉFONO?-------")
print(" Estamos interesados en comprar un nuevo teléfono móvil y en el escaparate\n de una tienda aparece que el móvil cuesta 420€. El problema es que si nos\n esperamos a comprarlo al día siguiente sufrirá un incremento porcentual\n del 20%. ¿Cuánto costará entonces el teléfono si nos esperamos?\n")

# solución
valor_inicial = 420.0
iva = (valor_inicial*(20/100))
valor_final = (valor_inicial + iva)
print(f"Si esperamos un día más, el teléfono nos costaría {valor_final} euros.")
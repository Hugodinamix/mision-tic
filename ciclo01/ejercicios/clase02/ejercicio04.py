print("-------¿CUÁNTAS LATAS DE REFRESCO SOBRAN?-------")
print("Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos,\ndonde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que \ntodas y cada una de ellas consuman la misma cantidad de refrescos\n¿Cuántas latas de refresco sobrarán? \n")
# Solución
cajas_refresco = 9
latasxcaja = 24
refrescos_totales = (latasxcaja * cajas_refresco)
total_invitados = 56

restante_refrescos = (refrescos_totales%total_invitados)

print(f"De los {refrescos_totales} refrescos que había, sobraron {restante_refrescos} latas después de que todos los invitados \ntomaran la misma cantidad de refrescos.")
def cliente(informacion:dict) -> dict:
    datos_cliente = dict()
    apto = True
    edad_cliente = informacion['edad']

    if edad_cliente > 18:
        atraccion = 'X-Treme'
        valor_boleta = 20000

        if informacion['primer_ingreso'] == True:   
            porcentaje_descuento = (valor_boleta*(5/100));
            valor_boleta = valor_boleta - porcentaje_descuento
    elif edad_cliente <= 18 and edad_cliente >= 15:
        atraccion = 'Carros chocones'
        valor_boleta = 5000
            
        if informacion['primer_ingreso'] == True:   
            porcentaje_descuento = (valor_boleta*(7/100));
            valor_boleta = valor_boleta - porcentaje_descuento
    elif edad_cliente <= 15 and edad_cliente >= 7:
        atraccion = 'Sillas voladoras'
        valor_boleta = 10000   
        if informacion['primer_ingreso'] == True:   
            porcentaje_descuento = (valor_boleta*(5/100));
            valor_boleta = valor_boleta - porcentaje_descuento
    else:
        apto = False,
        atraccion = 'N/A'
        valor_boleta = 'N/A'
    # inserción de datos
    datos_cliente['nombre'] = informacion['nombre']
    datos_cliente['edad'] = edad_cliente
    datos_cliente['atraccion'] = atraccion 
    datos_cliente['apto'] = apto
    datos_cliente['primer_ingreso'] = informacion['primer_ingreso']
    datos_cliente['total_boleta'] = valor_boleta 
    
    return datos_cliente 

def CDT(usuario: str, capital: int, tiempo: int):
    """
    --parametros-- 
    usuario(str): alfanumérico que
    identifica al usuario.
    capital(int): monto de dinero
    tiempo(int): tiempo del CDT
    """
    calculo = tiempo
    if tiempo > 2:
        intereses = capital * 0.03 * tiempo / 12
        calculo = intereses + capital
    elif tiempo <= 2:
        porcentaje_perdidas = capital * 0.02
        calculo = capital - porcentaje_perdidas
    
    mensaje = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {calculo}"
    return mensaje
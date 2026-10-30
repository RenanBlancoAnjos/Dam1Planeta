def espejo(texto):
    salida=""
    for i in range(len(texto)-1,-1,-1):
        salida +=texto[i]
    return salida
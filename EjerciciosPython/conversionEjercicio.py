def reverso (cadena):
    salida=""
    for i in range(len(cadena)-1,-1,-1):
        salida+=cadena[i]
    return salida

if __name__ == "__main__":
    print (reverso ("hasta mañana a las 8"))
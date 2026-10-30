

if __name__ == "__main__":


    n = int(input("Dime cuántos números vas a introducir: "))

    if n <= 0:
        print("La cantidad tiene que ser mayor que 0.")
    else:
        suma = 0
        maximo = 0
        minimo = 0

        for i in range(n):
            numero = float(input(f"Dime el número {i + 1}: "))
            suma += numero

            if maximo is None or numero > maximo:
                maximo = numero

            if minimo is None or numero < minimo:
                minimo = numero

        media = suma / n

        print(f"La suma es: {suma}")
        print(f"La media es: {media}")
        print(f"El máximo es: {maximo}")
        print(f"El mínimo es: {minimo}")
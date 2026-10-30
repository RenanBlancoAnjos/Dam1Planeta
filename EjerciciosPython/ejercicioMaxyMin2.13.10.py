













if __name__ == "__main__":
    #campo de existencia -&,+&
    
    numero=float(input("Introduce el numero "))
    maximo=minimo=numero

    for i in range (2,6):
        numero=float(input("Introduce el numero "))
        if(numero>maximo):
            maximo=numero
        elif(numero<minimo):
            minimo=numero


    print(f"el minimo:{minimo}\nEl máximo: {maximo}")

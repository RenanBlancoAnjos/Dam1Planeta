


if __name__ == "__main__":
    #notal^[0,10]

    maximo=-1
    minimo=11
    cmaximo=cminimo=0

    for i in range(1,6):
        nota=float(input("dime la nota "))
    
        if (nota>maximo):
            maximo=nota
            cmaximo=1
        elif (nota==maximo):
            cmaximo+=1


        if (nota<minimo): 
            minimo=nota
            cminimo=1
        elif (nota==minimo):
            cminimo+=1

    print(f"maxima nota {maximo}\nNota Minima {minimo}")
    print(f"la nota maxima se repetio {cmaximo}\nLa nota minima se repetio {cminimo}")
   

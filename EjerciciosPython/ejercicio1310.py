if __name__ == "__main__":
    numero=0
    
    cpares=cimpares=0
    while (True):
        
        n=int(input("introduce un numero "))
        if (n<0):break
        if (n%2==0):
            cpares+=1
        else:
            cimpares+=1

print(f"numero de parede: {cpares}\n numero de impares: {cimpares}")
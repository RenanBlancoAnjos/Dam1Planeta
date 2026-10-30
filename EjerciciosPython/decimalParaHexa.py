import math


def decimalAbinario(numero):
    binario=""
    while(numero>0):
        resto=numero%2
        binario=str(resto)+binario
        numero=numero//2
    return binario




def decimalAhexadecimal(n):
    cadena="0123456789ABCDEF"
    binario=""
    while(n>0):
        resto=n%16
        binario=cadena[resto:resto+1]+binario
        n=n//16
    return binario

def hexadecimalAdecimal(cadena):
    ca="0123456789ABCDEF"
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma +=ca.find(cadena[i:i+1])*math.pow(16,j)
        j+=1
    return suma



def decimalAoctal(n):
    cadena="0123456789ABCDEF"
    binario=""
    while(n>0):
        resto=n%8
        binario=str(resto)+binario
        n=n//8
    return binario


def octalAdecimal(cadena):
    n=len(cadena)-1
    suma=0
    j=0
    for i in range (n,-1,-1):
        suma +=int(cadena[i:i+1])*math.pow(8,j)
        j+=1
    return suma


if __name__ == "__main__":

    print(hexadecimalAdecimal("FF"))
    print(octalAdecimal("377"))
    while(True):
        n=int(input("Dime el numero "))
        if (n<0): break
        print(decimalAbinario(n))
        print(decimalAhexadecimal(n))
        print(decimalAoctal(n))
        
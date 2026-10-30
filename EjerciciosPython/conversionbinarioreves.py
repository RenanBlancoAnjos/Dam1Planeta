import math

def binarioAdecimal(cadena):

    n=len(cadena)-1
    #cadena 111
    j=0
    suma=0
    for i in range(n,-1,-1):
        suma +=int(cadena[i])*math.pow(2,j)
        j+=1
    return suma





def decimalAbinario(numero):
    binario=""
    while(numero>0):
        resto=numero%2
        binario=str(resto)+binario
        numero=numero//2
    return binario
   




if __name__ == "__main__":
    #n=int(input("Dime el numero decimal: "))
    #rint(decimalAbinario(n))
    print (binarioAdecimal("111"))



    def letradni(numero):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"
    n=numero%23
    return cadena[n]


def letranie(texto):
    #Z5034722 ------>G

    texto=str("XYZ".index(texto[0]))+texto[1:]
    return letradni(int(texto))
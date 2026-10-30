

def decimalAbinario(numero):
    binario=""
    while(numero>0):
        resto=numero%2
        binario=str(resto)+binario
        numero=numero//2
    return binario




if __name__ == "__main__":
    n=int(input("Dime el numero decimal: "))
    print(decimalAbinario(n))
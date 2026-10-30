def reverso(n):
    






if __name__ == "__main__":
    n=int(input("Dime el nº "))
    digito=int(input("Dime el digito "))
    ca=""
    n=reverso(n)
    c=0
    while (n>0):
        resto=n%10
        c +=1
        if(resto==digito):
            print(c,end="  ")
        n=n//10
def isPrimo(n):

    for i in range (2,n):
        if (n%i==0): return False
        return True
    
if __name__ == "__main__":
    print(isPrimo(7))
    print(isPrimo(22))
    
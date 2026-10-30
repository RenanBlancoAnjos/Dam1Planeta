def letraniedni(texto):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"
    n="XYZ".find(texto[0])
    if (n==-1):
       m=int(texto)%23
       return cadena[n]
    else:
       m=int(str(n)+texto[1:])%23
    
    return cadena[m]

#primeiro=texto[0]:
    if primero=="X":
        texto="0"+texto[1:]
    elif primero=="Y":
        texto="1"+texto[1:]
    elif primero=="Z":
        
     texto="2"+texto[1:]

    return letradni(int(texto))

if __name__ == "__main__":
   dni="50691319"
   print(dni,letraniedni(dni))
   nie="Z5034722"
   print (nie,letraniedni(nie))
nota=int(input("dime una nota"))


if (nota<0) or (nota>10):
    nota="fuera de rango"
elif (nota<5):
    nota= ("suspenso")
elif (nota<6):
    nota= ("aprobado")
elif (nota<7):
    nota= ("bien")
elif (nota<9):
    nota= ("notable")
elif (nota<=10):
    nota= ("sobressalente")
print(nota)

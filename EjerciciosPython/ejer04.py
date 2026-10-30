n=int(input("dime un mes"))


if n>=10 and n<=12:
    print("4 trimestre")
elif n<=9 and n>6:
    print("3 trimestre")
elif n<=6 and n>3:
    print("2 trimestre")
elif n<4 and n>=1:
    print("1 trimestre")
else:
    print ("El numero de mes tiene que estar entre 1 y 12")

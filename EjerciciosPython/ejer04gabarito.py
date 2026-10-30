n=int(input("dime un mes"))


if not (n>=1 and n<=12):
    print ("El numero de mes tiene que estar entre 1 y 12")
elif n<=3:
    print("1 trimestre")
elif n<=6:
    print("2 trimestre")
elif n<=9:
    print("3 trimestre")
else:
    print("4 trimestre")
n=int(input("dime un mes"))
m=int(input("dime un dia"))

z=((n*100)+m)

if (z<101) or (z>1231):
    signo="fuera de rango"
elif ((z>=101 and z<=119) or (z>=1222 and z<=1231)):
    signo= ("capricornio")
elif z<=218:
    signo=("aquario")
elif z<=320:
    signo=("peixes")
elif z<=419:
    signo=("aries")
elif z<=520:
    signo=("touro")
elif z<=620:
    signo=("gemeos")
elif z<=722:
    signo=("cancer")
elif z<=822:
    signo=("leao")
elif z<=922:
    signo=("virgem")
elif z<=1022:
    signo=("libra")
elif z<=1121:
    signo=("escorpiao")
elif z<=1221:
    signo=("sagitario")

print (signo)
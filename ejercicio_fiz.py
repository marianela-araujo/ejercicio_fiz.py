#lista denumeros de 1 al 100
# si es multiplo de 3 es fizz
#si es multiplo de 5 es buzz
# y sicumple las 2 funciones es fizzbuzz
# y si no cumple ninguna de las 2 los pongo en un
for numero in range (1,100):
    if numero %3==0 and numero %5==0:
        print((numero),"fizzbuzz")
    elif numero%5==0:
        print((numero),"buzz")
    elif numero%3==0:
        print((numero),"fizz")
    else:
        print((numero),"no cumple")
print(numero)
    
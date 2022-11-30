#lista denumeros de 1 al 100
# si es multiplo de 3 es fizz
#si es multiplo de 5 es buzz
# y si es multiplo de 3 y 5 es fizzbuzz
# y si no es divisible, nocumple no con las condiciones dadas 

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print((number),"FizzBuzz")
    elif number % 5 == 0:
        print((number),"Buzz")
    elif number % 3 == 0:
        print((number),"Fizz")
    else:
        print((number),"no cumple")
print (number)

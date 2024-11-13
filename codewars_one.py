# abs, prod, .is_integer(), 

#------------------------Problem------------------------------- 
# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8. 
# Your function will be tested with pre-made examples as well as random ones. 

from math import prod 
def find_difference(a, b):
    result = abs(prod(a) - prod(b))
    print(f"The difference of cuboids a[2,2,3] and b[5,4,1] is: {result}")

a=[2,2,3]
b=[5,4,1]
find_difference(a,b)
#---------------------------EXPLANATION---------------------------
# we import math to use prod
# prod(a): Calcula el producto de todos los elementos en el iterable a. Por ejemplo, si a = [2, 3, 4], entonces prod(a) devuelve 2 * 3 * 4 = 24.
# prod(b): Similarmente, calcula el producto de todos los elementos en el iterable b.
# prod(a) - prod(b): Resta el producto de b al producto de a.
# abs(...): Toma el valor absoluto de la diferencia obtenida en el paso anterior, asegurando que el resultado sea positivo.


c_first_number = float(input(f"Please enter your first number: "))
c_second_number = float(input(f"Please enter your second number: "))
c_third_number = float(input(f"Please enter your third number: "))
product_c = c_first_number * c_second_number * c_third_number 

# Función auxiliar para eliminar decimales si el número es entero
def mostrar_sin_decimal(number):
    return int(number) if number.is_integer() else number 


print(f"This 3 numbers form the first array assigned with letter c[{mostrar_sin_decimal(c_first_number)}, " f"{mostrar_sin_decimal(c_second_number)}, {mostrar_sin_decimal(c_third_number)}] \n" "Down below we will conform the array assigned to letter d.")


d_first_number = float(input(f"Please enter for d array your first number: "))
d_second_number = float(input(f"Please enter your second number: "))
d_third_number = float(input(f"Please enter your third number: "))

print(f"The 3 numbers form the second array asinged with letter d[{d_first_number}, {d_second_number}, {d_third_number}]")

c_array = [c_first_number, c_second_number, c_third_number]
b_array = [d_first_number, d_second_number, d_third_number]

def second_difference(c,d):
    result = abs(prod(c)-prod(d))
    print(f"The difference between your two arrays is: {result}")
    
second_difference(c_array, b_array)
'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez,
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista1 = [20, 50, "Curso", 'Python', 3.14]
print(lista1)
num1= int(input("1er número: "))
num2= int(input("2do número: "))

print(num1)
print(num2)

lista1.insert(0,num1) , lista1.insert(1,num2)
print(lista1)
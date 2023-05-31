#Si riman o no
print("**** Te digo si tus palabras riman o no ****")
palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman")
elif palabra1[-3:] == palabra2[-3:]:
    print("Si riman")
else:
    print("No rima parcero")
num1 =  int(input("Escreva o primeiro numero: "))
num2 =  int(input("Escreva o segundo numero: "))
num3 =  int(input("Escreva o terceiro numero: "))

if num1 >= num2 and num1 >= num3:
    print("O maior número é",num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é",num2)
elif num3 >= num1 and num3 >= num2:
    print("O maior número é",num3)

else:
    print("Todos os números são iguais")
    





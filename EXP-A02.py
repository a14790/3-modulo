
#B1
# i = 1

# while i < 11:
#   print(i)
#   i += 1

# B2

# i = 10

# while i >= 1:
#   print(i)
#   i -= 1

#B3
# for i in range (21):
#     print(i)

#B4

# for i in range (0 , 22, 2):
#     print(i)

#I1

# soma = 0
# for i in range(1, 101):
#     soma += i
#     print(f'A soma de {i} é : {soma}')


#I2

# num = 0
# while num >= 0:
#     num = int(input("Digite um número: "))
# print("Programa encerrado")


#I3
# num_pares = 0
# for i in range (0, 51, 2):
#     print(i)
#     num_pares += 1
# print(num_pares)



#A1
# nums = 0
# quantos_nums = int(input("Quantos números quer colocar: "))
# for i in range((quantos_nums)):
#     nums += int(input("Insira os seus números: "))
# print(f'A sua soma é de : {nums}')


#A2

# opcao = -1

# while opcao != 0:
#     print("MENU")
#     print("1 - Mostrar números de 1 a 10")
#     print("2 - Mostrar números pares até 20")
#     print("0 - Sair")

#     opcao = int(input("Escolha uma opção: "))

#     if opcao == 1:
#         for i in range(1, 11):
#             print(i)

#     elif opcao == 2:
#         for i in range(2, 21, 2):
#             print(i)

#     elif opcao == 0:
#         print("Programa encerrado.")

#     else:
#         print("Opção inválida!")
#A3

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print(numero, "! =", fatorial)
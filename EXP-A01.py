# B1

# num = float(input("Digite um número: "))

# if num >= 0:
#     print("O seu número é positivo")

# else:
#     print("O seu número é negativo")

# # B2
 
# idade = int(input("Digite a sua idade: "))

# if idade <= 18:
#     print("Menor de idade")

# else:
#     print("Maior de idade")

#B3

# num = int(input("Digite um número: "))

# if num % 2 == 0:
#     print("O seu número é par ")

# else:
#     print("O seu número é impar")

# # B4

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# if num1 > num2:
#     print("O maior numero é:",num1)
# else:
#     print("O maior numero é:",num2)

#B5

# password = str(input("Digite a password: "))

# if password == "python":
#     print("Acesso permitido")
# else:
#     print("Acesso negado")


# # I1
# nota = int(input("Qual a sua nota? "))

# if nota < 10:
#     print("REPROVADO")
# elif nota >= 11 and nota <= 13:
#     print("SUFICIENTE")
# elif nota >= 14 and nota <= 17:
#     print("BOM")
# else:
#     print("EXCELENTE")

# # I2

# idade = int(input("Qual a sua idade? "))

# if idade < 13:
#     print("És uma criança")
# elif idade >= 13 and idade <= 17:
#     print("És um jovem")
# elif idade >= 18 and idade <= 64:
#     print("És um adulto")
# else:
#     print("És um sénior")

# # I3
 
# num = int(input("Digite um número: "))
 
# if num % 3 == 0:
#     print("O número é multiplo de 3")

# elif num % 5 ==0:
#     print("O número é multiplo de 5")

# elif num % 3 ==0 and num % 5 == 0:
#     print("O número é multiplo de 3 e de 5")

# else:
#     print("O número não tem múltiplos ")

#I4

# utilizador_correto = "admin"
# password_correto = 1234

# utilizador = str(input("Insira a utilizador: "))
# password = int(input("Intruduza a password: "))

# if utilizador != utilizador_correto:
#     print("O seu utilizador está errado")
# elif password != password_correto:
#     print("A sua password está errada")
# elif utilizador == utilizador_correto and password == password_correto:
#     print("A sua password e o seu utilizador estão corretos")

    

# # I5

# num = int(input("Insira um número: "))

# if num >= 10 and num <= 20:
#     print("O seu número está entre 10 e 20")
# else:
#     print("O seu número não está entre 10 e 20")

# A1

saldo_inicial = 1000

valor_levantar = int(input("Insira o valor a lenvantar: "))

if saldo_inicial >= valor_levantar:
    print("autorizado")
else:
    print("saldo insuficiente")


# A2

num1 =  int(input("Escreva o primeiro numero: "))
num2 =  int(input("Escreva o segundo numero: "))
num3 =  int(input("Escreva o terceiro numero: "))
num4 =  int(input("Escreva o quarto numero: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print("O maior número é",num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("O maior número é",num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("O maior número é",num3)
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    print("O maior número é",num4)

# A3

peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))
IMC = peso / (altura * altura)


if IMC < 18.5:
    print("Baixo peso")
elif IMC <=18.5 and IMC > 24.9:
    print("Normal")
elif IMC <=25 and IMC >= 29.9:
    print("Excesso de peso")
else:
    print("Obsidade")

# A4

valor = int(input("Digite o seu valor de compra: "))
desconto = 0
if valor >= 100:
    desconto = valor * 0.1
    valor_final = valor - desconto 
    print("O seu desconto é: ",desconto)
    print(f"O seu desconto nesta compra é de {desconto} o seu valor final a pagar é de {valor_final} .")

elif valor >= 50:
    desconto = valor * 0.05
    valor_final = valor - desconto 
    print("O seu desconto é: ",desconto)
    print(f"Não tem nenhum desconto nesta compra e o seu valor final a pagar é de {valor_final} .")


# A5

ano = int(input("Insira o ano: "))

if ano % 4 == 0:
    print(f'O seu ano {ano} é bissexto')
else:
    print(f'O ano {ano} é um ano normal')
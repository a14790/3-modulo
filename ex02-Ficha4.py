idade = int(input("Qual a sua idade? "))

if idade < 13:
    print("És uma criança")
elif idade >= 13 and idade <= 17:
    print("És um jovem")
elif idade >= 18 and idade <= 64:
    print("És um adulto")
else:
    print("És um sénior")

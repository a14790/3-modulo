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
else: 
    print(f"Não tem nenhum desconto nesta compra e o seu valor final a pagar é de {valor_final} .")
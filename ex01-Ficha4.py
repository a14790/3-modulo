saldo = 100
valor_levantar = float(input("Digite o seu valor a levantar: "))

restante = saldo - valor_levantar

if saldo >= valor_levantar:
    print("Autorizar")
    print(f"O valor restante da sua conta é {restante} euros.")
else:
    print("Rejeitar")
    print(f"Não irá concluir a tranferência pois irá ficar com {restante} euros na conta.")



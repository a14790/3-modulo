notas = []


def adicionar_nota():
    while True:
        nota = int(input("Introduz uma nota entre 0 e 20: "))

        if 0 <= nota <= 20:
            notas.append(nota)
            print("Nota adicionada com sucesso.")
            break
        else:
            print("Erro: a nota tem de estar entre 0 e 20.")


def listar_notas():
    if len(notas) == 0:
        print("Ainda não existem notas registadas. ")
    else:
        print("Lista de notas: ")
        for n in notas:
            print(n)



def calcular_media():
    if len(notas) == 0:
        print("Não existem notas para calcular média. ")
    else:
        soma = 0
        for n in notas:
            soma = soma + n
        
        media = soma / len(notas)
        print("Média das notas:", media) 



def mostrar_positivas():
    if len(notas) == 0:
        print("Não existem notas registadas. ")
    else:
        print("Notas positivas: ")
        for n in notas:
            if n >= 10:
                print(n)



while True:
    print("1 Adicionar nota")
    print("2 Listar notas")
    print("3 Calcular média")
    print("4 Mostrar notas positivas")
    print("0 Sair")

    opcao = input("Escolhe uma opção: ")

    if opcao == "1":
        adicionar_nota()
    elif opcao == "2":
        listar_notas()
    elif opcao == "3":
        calcular_media()
    elif opcao == "4":
        mostrar_positivas()
    elif opcao == "0":
        print("Programa terminado. ")
        break
    else:
        print("Opção inválida. Tenta novamente. ")
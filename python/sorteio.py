import random
opcao = -1
nomes = []


def inserir():
    qtdPessoas = int(input("Quantas pessoas deseja inserir? "))
    for i in range(qtdPessoas):
        nome = input("Digite o nome que deseja inserir: ")
        nomes.append(nome)
def listar():
    print("Os nomes inseridos são: ")
    for nome in nomes:
        print(nome)
def sortear():
    sorteado = random.choice(nomes)
    print("O nome sorteado foi: " + sorteado)    

while opcao != 4:
    print('''
    Digite uma das seguintes opções:
    1 - para inserir um nome
    2 - ver os nomes
    3 - sortear um nome
    4 - sair
    ''')
    opcao = int(input("insira a opção desejada: "))

    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        sortear()
    elif opcao == 4:
        print("saindo do programa...")
    else:
        print("opção inválida, tente novamente")



    
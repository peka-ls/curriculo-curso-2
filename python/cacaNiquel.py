import random
inicio = -1
numeros1 = [1, 2, 3, 4, 5, 6, 7]
numeros2 = [1, 2, 3, 4, 5, 6, 7]
numeros3 = [1, 2, 3, 4, 5, 6, 7]

def sorteio1():
    numeroSorteado = random.choice(numeros1)
    print("O número sorteado foi:" + str(numeroSorteado))

def sorteio2():
    numeroSorteado = random.choice(numeros2)
    print("O número sorteado foi:" + str(numeroSorteado))

def sorteio3():
    numeroSorteado = random.choice(numeros3)
    print("O número sorteado foi:" + str(numeroSorteado))

while inicio != 2:
    print('''
Digite uma das seguintes opções:
1 - Girar a roleta
2 - Sair
''')
    inicio = int(input("Insira a opção desejada: "))
    if inicio == 1:
        srtNum1 = sorteio1()
        srtNum2 = sorteio2()
        srtNum3 = sorteio3()
        if srtNum1 == srtNum2 == srtNum3:
            print("JACKPOT!!! Você ganhou o prêmio máximo!")
        elif srtNum1 == srtNum2 or srtNum1 == srtNum3 or srtNum2 == srtNum3:
            print("Parabéns! Você ganhou um prêmio menor!")
        else:
            print("Infelizmente, você não ganhou nenhum prêmio. Tente novamente!")
    elif inicio == 2:
        print("Tem certeza que deseja sair? A maioria das pessoas para antes de um grande prêmio (S/N)")
        resposta = input("Digite S para sim ou N para não: ")
        if resposta.upper() == "S":
            print("Saindo do programa...")
        elif resposta.upper() == "N":
            print("Voltando para o menu...")
        else:
            print("Resposta inválida, voltando para o menu...")
    else: 
        print("Opção inválida, tente novamente")


import random
inicio = -1
numeros = [1, 2, 3, 4, 5, 6, 7]

# def sorteio1():
#     numero1Sorteado = random.choice(numeros)
#     print("O número sorteado foi:" + str(numero1Sorteado))

# def sorteio2():
#     numero2Sorteado = random.choice(numeros)
#     print("O número sorteado foi:" + str(numero2Sorteado))

# def sorteio3():
#     numero3Sorteado = random.choice(numeros)
#     print("O número sorteado foi:" + str(numero3Sorteado))

while inicio != 2:
    print('''
Digite uma das seguintes opções:
1 - Girar a roleta
2 - Sair
''')
    inicio = int(input("Insira a opção desejada: "))
    if inicio == 1:
        srtNum1 = numero1Sorteado = random.choice(numeros)
        print("O número sorteado foi:" + str(numero1Sorteado))
        srtNum2 = numero2Sorteado = random.choice(numeros)
        print("O número sorteado foi:" + str(numero2Sorteado))
        srtNum3 = numero3Sorteado = random.choice(numeros)
        print("O número sorteado foi:" + str(numero3Sorteado))
        
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


nomeAluno = input("digite o nome do aluno: ")
nota1 = int(input("digite a nota do primeiro trimestre: "))
nota2 = int(input("digite a nota do segundo trimestre: "))
nota3 = int(input("digite a nota do terceiro trimestre: "))
nota4 = int(input("digite a nota do quarto trimestre: "))
media = (nota1 + nota2 + nota3 + nota4) /4

#if(media >= 70):
 #   print("parabéns " + nomeAluno + ", você foi aprovado com a média de : " +str(media))
#else:
#    print("infelizmente " + nomeAluno + ", você foi reprovado com a média de : " +str(media))

if(media >= 90):
    print("PARABÉNS! você foi aprovado com a média de: " +str(media))
elif(media >= 80 and media < 90):
    print("Otimo! você foi aprovado com a média de: " + str(media))
elif(media >=70 and media < 80):
    print("Bom! você foi aprovado com a média de: " + str(media))
elif(media >= 60 and media <70):
    print("Passou perto! Mas infelizmente você foi reprovado com a média de: " + str(media))
else:
    print("Dessa vez não deu, infelizmente você foi reprovado com a média de: " +str(media))


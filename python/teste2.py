valorAlcool = float(input("digite o valor da alcool "))
valorGasolina = float(input("digite o valor do gasolina " ))
consumoGasolina = float(input("digite o seu consumo de gasolina por km "))
consumoDeAlcool = float(input("digite o seu consumo de alcool por km "))
qtdPessoas = int(input("digite a quantidade de pessoas no carro "))
distanciaKm = 100
 
gastoGasolina = (distanciaKm / consumoGasolina) * valorGasolina
gastoAlcool = (distanciaKm / consumoDeAlcool) * valorAlcool
gasolinaPorPessoa = gastoGasolina / qtdPessoas
alcoolPorPessoa = gastoAlcool / qtdPessoas




if(gastoGasolina > gastoAlcool):
    print("O valor total da gasolina será de: " + str(gastoGasolina) + " e o de alcool será: " + str(gastoAlcool) +" portanto, abasteça com alcool")
else:
    print("O valor total da alcool será de: " + str(gastoAlcool) + " e o de gasolina será: " + str(gastoGasolina) +" portanto, abasteça com gasolina")    

if(gastoGasolina > gastoAlcool):
    print("O valor total do alcool será de " + str(gastoAlcool) + " e o custo por pessoa é de: " + str(alcoolPorPessoa))
else:
    print("O valor total da gasolina será de " + str(gastoGasolina) + " e o custo por pessoa é de: " + str(gasolinaPorPessoa))
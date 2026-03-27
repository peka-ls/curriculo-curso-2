alcool = float(input("digite o valor da alcool "))
gasolina = float(input("digite o valor do gasolina " ))
consumoGasolina = float(input("digite o seu consumo de gasolina por km "))
consumoDeAlcool = float(input("digite o seu consumo de alcool por km "))
distanciaKm = 100
 
gastoGasolina = (distanciaKm / consumoGasolina) * gasolina
gastoAlcool = (distanciaKm / consumoDeAlcool) * alcool



if(gastoGasolina > gastoAlcool):
    print("abasteça com alcool")
else:
    print("abasteça com gasolina")    
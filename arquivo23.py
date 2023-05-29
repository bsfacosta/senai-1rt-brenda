velocidade = float(input("Informe a velocidade do seu veiculo: "))

if velocidade >= 80:
    print("Voce esta acima da velocidade permitida e foi multado no valor de R${}.".format((velocidade-80)*7)) 

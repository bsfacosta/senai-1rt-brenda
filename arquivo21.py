distancia = float(input("Informe a distancia: "))

if distancia <= 200:
    print("O valor da sua passagem sera de R${}".format(distancia*0.50))

elif distancia > 200:
    print("O valor da sua passagem sera de R${}".format(distancia*0.45))
    
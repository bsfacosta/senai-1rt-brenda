n1 = float(input("Informe o primeiro valor:"))
n2= float(input("Informe o segundo valor: "))
imput = "adicao", "subtracao","divisao","multiplicacao"
imput = input("Insira o metodo de calculo (adicao, subtracao, divisao ou multiplicacao): ")

if imput == "adicao":
    print(n1+n2)
if imput == "subtracao":
    print(n1-n2)
if imput == "divisao":
    print(n1/n2)
if imput == "multiplicacao":
    print(n1*n2)


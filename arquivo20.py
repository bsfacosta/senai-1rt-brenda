salario = float(input("Informe o seu salario: "))

if salario > 8250:
  print("Seu atual salário com o reajuste é R${}".format(salario*0.10 + salario))
elif salario <= 8250:
  print("Seu atual salário com o reajuste é R${}".format(salario*0.15 + salario))



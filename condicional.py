nota1 = float(input("Sua nota de matematica é: "))
nota2 = float(input("Sua nota de biologia é: "))
nota3 = float(input("Sua nota de historia é: "))

media = (nota1+nota2+nota3)/3

print("Sua média é igual a: {:.2f} ".format(media))

if media >= 6:
    print("Voce foi aprovado")

else:
    print("Voce foi reprovado")
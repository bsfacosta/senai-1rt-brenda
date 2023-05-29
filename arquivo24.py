pontuacao = int(input("Informe sua pontuação da olimpíada do Senai: "))

if pontuacao <= 50:
    print("Parabens! Voce ganhou o certificado de participacao")

elif pontuacao <= 60:
    print("Parabens! Voce ganhou o certificado de mencao honrosa")

elif pontuacao <= 70:
    print("Parabens! Voce ganhou a medalha de bronze")

elif pontuacao <= 90:
    print("Parabens! Voce ganhou a medalha de prata")

elif pontuacao > 90:
    print("Parabens! Voce ganhou a medalha de ouro")

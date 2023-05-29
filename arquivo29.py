num = int(input("Informe um numero: "))

print("Tabuada do numero",num,":")
for cont in range(1,11):
    resultado = num * cont
    print(num, "x" , cont,"=",resultado)
    

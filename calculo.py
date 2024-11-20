x = float(input('digite o primeiro numero '))
y = float(input('digite o segundo numero '))
z = float(input('digite o terceiro numero '))
media = (x * 1 + y * 1 + z * 2) / (4)
print(media)
if media > 6:
    print("aprovado")
else:
    if media >= 5 <= 6:
        print("recuperacao")
    else:
        if media < 5 >= 0:
            print("reprovado")

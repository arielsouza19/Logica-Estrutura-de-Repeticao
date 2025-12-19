soma = 0
cont = 0
idade = 1

while idade != 0:
    idade = int(input("Digite a idade: "))
    if idade != 0:
        soma += idade
        cont += 1

media = soma / cont
print(media)

import random

input("Digite JOGAR para lançar o dado:")

resultado = 0

for dado in range(2):
    resultado += random.randint(1, 6)

print(f"Primeira jogada: {resultado}")

if resultado in (7, 11):
    print("natural, você ganhou")

elif resultado in (2, 3, 12):
    print("craps, você perdeu")

else:
    ponto = resultado

    print(f"Seu ponto é: {ponto}")

    while True:

        input("Digite JOGAR para lançar o dado novamente: ")

        resultado = 0

        for dado in range(2):
            resultado += random.randint(1, 6)

        print(f"Você tirou: {resultado}")

        if resultado == ponto:
            print("Você tirou seu ponto novamente! Ganhou!")
            break

        elif resultado == 7:
            print("Você tirou 7! Perdeu!")
            break
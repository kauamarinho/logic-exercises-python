# Leia 5 números do usuário e informe qual foi o maior e o menor entre eles

primeiro = int(input("Digite o 1º número: "))
maior = primeiro
menor = primeiro

for i in range(2, 6):
    numero = int(input(f"Digite o {i}º número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
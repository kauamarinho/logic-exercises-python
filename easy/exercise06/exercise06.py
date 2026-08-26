# Peça um número N ao usuário e exiba todos os números de 1 até N informando se cada um é par ou ímpar.

n = int(input(f"Me informe um numero: "))

par = n
impar = n

for i in range(n, n + 1):
    if n != par:
        print(f"O número é Impar")
    else:
        print(f"O númeoro é Par")

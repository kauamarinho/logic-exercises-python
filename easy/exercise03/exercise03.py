
# Peça ao usuário quantos números ele quer somar. Leia cada número e exiba a soma total no final.

n = int(input("Quantos números você quer somar? "))

soma = 0

for i in range(1, n + 1):
    numero = float(input(f"Digite o {i}º número: "))
    soma = soma + numero

print(f"\nA soma dos {n} números é: {soma}")
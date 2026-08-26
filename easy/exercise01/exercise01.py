# Contagem regressiva

# Peça um número inteiro positivo ao usuário e exiba uma contagem regressiva de N até 0.


numero = int(input(f"Me de um Número para a contagem regressiva até o 0: " ))

for numero in range(numero, 0 , - 1):
    print(numero)


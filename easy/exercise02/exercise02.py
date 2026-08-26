# Tabuada

# Peça um número e exiba a tabuada completa dele (de 1 a 10).

n = int(input("Digite um número: "))

print(f"\nTabuada do {n}:")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
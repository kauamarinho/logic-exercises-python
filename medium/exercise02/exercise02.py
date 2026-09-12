numbers = []
for i in range(8):
    value = int(input(f'Enter number {i + 1}: '))
    numbers.append(value)

largest = numbers[0]
smallest = numbers[0]
largest_position = 1

for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
        largest_position = i + 1  # +1 because index starts at 0
    if numbers[i] < smallest:
        smallest = numbers[i]

range_value = largest - smallest

print(f'Largest value: {largest}')
print(f'Smallest value: {smallest}')
print(f'Range: {range_value}')
print(f'The largest value was entered at position: {largest_position}')
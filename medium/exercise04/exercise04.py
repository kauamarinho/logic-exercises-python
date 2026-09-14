def sort_values(values):
    for i in range(len(values)):
        for j in range(len(values) - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values


numbers = []

value = int(input("Enter a value: "))
numbers.append(value)

sorted_numbers = sort_values(numbers)

print(sorted_numbers)
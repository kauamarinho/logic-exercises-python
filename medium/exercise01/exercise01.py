num_employees = 0
while num_employees <= 0:
    num_employees = int(input('Enter the number of employees: '))
    if num_employees <= 0:
        print('The number must be positive!')

salaries = []
for i in range(num_employees):
    salary = -1
    while salary <= 0 or salary > 50000:
        salary = float(input('Enter the employee salary: '))
        if salary <= 0 or salary > 50000:
            print('The salary must be greater than zero and at most $50,000.00!')
    salaries.append(salary)

average = sum(salaries) / num_employees

above_average = 0
for s in salaries:
    if s > average:
        above_average += 1

print(f'Average salary: ${average:.2f}')
print(f'Employees above average: {above_average}')
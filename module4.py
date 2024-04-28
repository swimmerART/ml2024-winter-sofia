

def find_number(target, numbers):
    for a, b in enumerate(numbers, start=1):
        if b == target:
            return a
    return -1



N = int(input("Enter the number of elements (positive integer): "))
print(N)
numbers = []

for i in range(N):
  number = int(input(f"Enter number {i+1}: "))
  numbers.append(number)
print(numbers)

target = int(input("Enter the target number to search: "))

result = find_number(target, numbers)

if result == -1:
    print(-1)
else:
    print(result)

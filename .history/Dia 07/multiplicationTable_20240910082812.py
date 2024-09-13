number = int(input("Digite um número: "))

def multiplicationTable(number):
  result = 0
  for n in range(1, 11):
    result = number * n
    print(f"{n} * {number} = {result}")

multiplicationTable(number)
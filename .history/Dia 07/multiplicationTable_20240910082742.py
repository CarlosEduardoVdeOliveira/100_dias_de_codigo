number = float(input("Digite um número: "))

def multiplicationTable(number):
  result = 0
  for n in range(0, 10):
    result = number * n
    print(f"{n} * {number} = {result}")

multiplicationTable(number)
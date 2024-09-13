number = float(input("Digite um número: "))

def multiplicationTable(number):
  
  for n in range(1, 11):
    result = number * n
    print(f"{n} * {number} = {result}")

multiplicationTable(number)
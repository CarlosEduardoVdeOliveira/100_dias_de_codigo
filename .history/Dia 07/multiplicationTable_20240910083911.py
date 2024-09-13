number = float(input("Digite um número: "))

def multiplicationTable(number):
  print(f"Tabuada de {number}:")
  for n in range(1, 11):
    result = number * n
    print(f"{n} * {number} = {n*number}")

multiplicationTable(number)
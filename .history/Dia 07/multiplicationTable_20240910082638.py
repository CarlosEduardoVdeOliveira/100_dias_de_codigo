from tokenize import Double

number = (input("Digite um número: "))

def multiplicationTable(number):
  result = 0
  for n in range(1, 10):
    result = number * n
    print("{n} * {number} = {result}")
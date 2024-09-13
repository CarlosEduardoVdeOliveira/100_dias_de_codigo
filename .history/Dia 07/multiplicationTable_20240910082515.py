from tokenize import Double

number = Double(input("Digite um número: "))

def multiplicationTable(number):
  for n in range(1, 10):
    print("{n} * {number}")
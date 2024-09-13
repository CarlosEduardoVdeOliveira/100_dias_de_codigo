number = float(input("Digite um número: "))

def multiplicationTable(number):
  print(f"Tabuada de {number}:")
  for n in range(1, 11):
    result = number * n
    print(f"{n} * {number} = {n*number}")
while True:
    try:
        number = float(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite um número válido.")
        
multiplicationTable(number)
number = int(input("Digite um número: "))
def factorial(number):
  i = 0
  fat = 2
  while i <= number:
    if(number == 0 or number == 1):
      print(f"Fatorial de {number}: {1}")
      break
    fat = i * number
    print(fat)
    i += 1

factorial(number)
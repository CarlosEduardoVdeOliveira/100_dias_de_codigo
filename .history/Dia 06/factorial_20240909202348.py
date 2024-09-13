number = int(input("Digite um número: "))
def factorial(number):
  i = 0
  fat = 2
if(number == 0 or number == 1):
  print(f"Fatorial de {number}: {1}")
  break
  while i <= number:
    fat += i * number
    print(fat)
    i += 1

factorial(number)
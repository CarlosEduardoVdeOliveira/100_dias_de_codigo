number = int(input("Digite um número: "))
def factorial(number):
  i = 0
  fat = 2
  if(number == 0 or number == 1):
    return 1
  else:
    while i <= number:
      fat += i * number
      print(fat)
      i += 1

factorial(number)
number = int(input("Digite um número: "))
def factorial(number):
  i = 0
  if(number == 0 or number == 1):
    return 1
  else:
    while i <= number:
      fat = i * number
      i += 1

factorial(number)
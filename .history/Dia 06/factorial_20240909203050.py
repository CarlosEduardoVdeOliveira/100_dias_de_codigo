def factorial(number):
  i = 1
  if(number == 0 or number == 1):
    return 1
  else:
    fat = 1
    while i <= number:
      fat *= i
      i += 1
    return fat
  
number = int(input("Digite um número: "))

if(number < 0):
  print(f"Fatorial de {number} não existe.")
else:
  print(f"{number}! = {factorial(number)}")
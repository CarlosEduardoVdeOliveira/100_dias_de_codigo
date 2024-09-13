number = int(input("Digite um número: "))
def factorial(number):
  i = 0
  if(number == 0 or number == 1):
    return 1
  else:
    fat = 1
    while i <= number:
      fat = i * fat
      i += 1
    return fat

if(number < 0):
  print(f"Fatorial de {number} não existe.")
else:
  print(f"O fatorial de  {factorial(number)}")
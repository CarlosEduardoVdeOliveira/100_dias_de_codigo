number = int(input("Digite um número: "))
i = 0
fact = 1
while i <= number:
  if(number == 0 | number == 1):
    print()
  fact = i * number
  print(fact)
  i += 1

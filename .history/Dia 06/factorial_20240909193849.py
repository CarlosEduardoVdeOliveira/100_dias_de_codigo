number = int(input("Digite um número: "))
i = 0
fact = 1
while i <= number:
  if(number == 0 or number == 1):
    print("Fatorial de "+number+" : "+ 1)
    break
  fact = i * number
  """ print(fact) """
  i += 1

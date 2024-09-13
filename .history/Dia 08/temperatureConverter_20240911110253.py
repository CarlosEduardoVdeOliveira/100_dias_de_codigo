temperature = float(input("Digite a temperatura: "))
choose_conversion = int(input("Digite a opção de conversão: "))

def temperature_converet_celsius_to_fahrenheit(temperature):
  return "{:.2f}".format(temperature * 1.8 + 32)

def temperature_converet_fahrenheit_to_celsius(temperature):
  return "{:.2f}".format((temperature - 32 ) * (5 / 9))

def temperature_converet_celsius_to_kelvin(temperature):
  return "{:.2f}".format(temperature + 273.15)

def temperature_converet_kelvin_to_celsius(temperature):
  return "{:.2f}".format(temperature - 273.15)

def temperature_converet_fahrenheit_to_kelvin(temperature):
  return "{:.2f}".format((temperature - 32) * (5 / 9) + 273.15)

def temperature_converet_kelvin_to_fahrenheit(temperature):
  return "{:.2f}".format((temperature - 273.15) * (9 / 5) + 32)

def default_case():
  return "Escolha inválida"

switch = {
  1: temperature_converet_celsius_to_fahrenheit(temperature),
  2: temperature_converet_fahrenheit_to_celsius(temperature),
  3: temperature_converet_celsius_to_kelvin(temperature),
  4: temperature_converet_kelvin_to_celsius(temperature),
  5: temperature_converet_fahrenheit_to_kelvin(temperature),
  6: temperature_converet_kelvin_to_fahrenheit(temperature),
}
print("=========Menu===========")
print("Opção 1: celsius para fahrenheit(temperature), ")
print("Opção   2: fahrenheit para celsius(temperature), ")
print("Opção   3: celsius para kelvin(temperature), ")
print("Opção   4: kelvin para celsius(temperature), ")
print("Opção   5: fahrenheit para kelvin(temperature), ")
print("Opção   6: kelvin para fahrenheit ")
print(switch.get(choose_conversion, default_case)())
def temperature_converet_celsius_to_fahrenheit(temperature):
  result = "{:.2f}".format(temperature * 1.8 + 32) + " °F"
  return "Conversão de °C para °F: {}"

def temperature_converet_fahrenheit_to_celsius(temperature):
  result = "{:.2f}".format((temperature - 32 ) * (5 / 9)) + " °C"
  return "Conversão: °F para °C: {}"

def temperature_converet_celsius_to_kelvin(temperature):
  result = "{:.2f}".format(temperature + 273.15) + " °K"
  return "Conversão: °C para °K: {}"

def temperature_converet_kelvin_to_celsius(temperature):
  result = "{:.2f}".format(temperature - 273.15) + " °C"
  return "Conversão: °K para °C: {}"

def temperature_converet_fahrenheit_to_kelvin(temperature):
  result = "{:.2f}".format((temperature - 32) * (5 / 9) + 273.15) + " °K"
  return "Conversão: °F para °K: {}"

def temperature_converet_kelvin_to_fahrenheit(temperature):
  result = "{:.2f}".format((temperature - 273.15) * (9 / 5) + 32) + " °F"
  return "Conversão: °K para °F: {}"

def default_case():
  return "Escolha inválida.\nTente novamente."

print("=========Menu===========")
print("Opção 1: Celsius para Fahrenheit.")
print("Opção 2: Fahrenheit para Celsius.")
print("Opção 3: Celsius para Kelvin.")
print("Opção 4: Kelvin para Celsius.")
print("Opção 5: Fahrenheit para Kelvin.")
print("Opção 6: Kelvin para Fahrenheit.")
print("========================")
print("")

choose_conversion = int(input("Digite a opção de conversão: "))
temperature = float(input("Digite a temperatura: "))

switch = {
  1: temperature_converet_celsius_to_fahrenheit,
  2: temperature_converet_fahrenheit_to_celsius,
  3: temperature_converet_celsius_to_kelvin,
  4: temperature_converet_kelvin_to_celsius,
  5: temperature_converet_fahrenheit_to_kelvin,
  6: temperature_converet_kelvin_to_fahrenheit,
}

conversion_function = switch.get(choose_conversion, default_case)

if conversion_function == default_case:
    print(conversion_function())
else:
    print(conversion_function(temperature))
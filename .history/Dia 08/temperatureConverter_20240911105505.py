temperature = float(input("Digite a temperatura em Celsius: "))

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

switch ={
  1:
}
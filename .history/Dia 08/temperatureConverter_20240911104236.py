import math


temperature = float(input("Digite a temperatura em Celsius: "))

def temperatureConveretCelsiusToFahrenheit(temperature):
  return math.floor(temperature * 1.8 + 32)

def temperatureConveretFahrenheitToCelsius(temperature):
  return math.floor((temperature - 32 ) * (5 / 9))

def temperatureConveretCelsiusToKelvin(temperature):
  return math.floor(temperature + 273.15)

def temperatureConveretKelvinToCelsius(temperature):
  return math.floor(temperature - 273.15)

def temperatureConveretFahrenheitToKelvin(temperature):
  return math.floor((temperature - 32) * (5 / 9) + 273.15)

def temperatureConveretKelvinToFahrenheit(temperature):
  return math.floor((temperature - 273.15) * (9 / 5) + 32)


print(temperatureConveretKelvinToFahrenheit(temperature))
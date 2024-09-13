temperature = float(input("Digite a temperatura em Celsius: "))

def temperatureConveretCelsiusToFahrenheit(temperature):
  return temperature * 1.8 + 32

def temperatureConveretFahrenheitToCelsius(temperature):
  return (temperature - 32 ) * (5 / 9)

def temperatureConveretCelsiusToKelvin(temperature):
  return temperature + 273.15

def temperatureConveretKelvinToCelsius(temperature):
  return temperature - 273.15

def temperatureConveretFahrenheitToKelvin(temperature):
  return (temperature - 32) * (5 / 9) + 273.15

def temperatureConveretKelvinToFahrenheit(temperature):
  return (temperature - 273.15) * 1 + 32


print(temperatureConveretKelvinToFahrenheit(temperature))
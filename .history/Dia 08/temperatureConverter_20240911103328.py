temperature = float(input("Digite a temperatura em Celsius: "))

def temperatureConveretCelsiusToFahrenheit(temperature):
  return temperature * 1.8 + 32

def temperatureConveretFahrenheitToCelsius(temperature):
  return (temperature - 32 ) * 0.555

def temperatureConveretCelsiusToKelvin(temperature):
  return temperature + 273.15

def temperatureConveretFahrenheitToCelsius(temperature):
  return (temperature - 32 ) * 0.555


print(temperatureConveretCelsiusToFahrenheit(temperature))
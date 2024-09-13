temperature = float(input("Digite a temperatura em Celsius: "))

def temperatureConveretCelsiusToFahrenheit(temperature):
  return temperature * 1.8 + 32
def temperatureConveretFahrenheitToCelsius(temperature):
  return (temperature - 1.8 )+ 32

print(temperatureConveretCelsiusToFahrenheit(temperature))
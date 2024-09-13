temperature = float(input("Digite a temperatura em Celsius: "))
control = ""
def temperatureConveretCelsiusToFahrenheit(temperature):
  return "{:.2f}".format(temperature * 1.8 + 32)

def temperatureConveretFahrenheitToCelsius(temperature):
  return "{:.2f}".format((temperature - 32 ) * (5 / 9))

def temperatureConveretCelsiusToKelvin(temperature):
  return "{:.2f}".format(temperature + 273.15)

def temperatureConveretKelvinToCelsius(temperature):
  return "{:.2f}".format(temperature - 273.15)

def temperatureConveretFahrenheitToKelvin(temperature):
  return "{:.2f}".format((temperature - 32) * (5 / 9) + 273.15)

def temperatureConveretKelvinToFahrenheit(temperature):
  return "{:.2f}".format((temperature - 273.15) * (9 / 5) + 32)


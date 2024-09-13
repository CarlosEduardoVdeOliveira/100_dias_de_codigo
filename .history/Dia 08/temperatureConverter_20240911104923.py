temperature = float(input("Digite a temperatura em Celsius: "))
control = ""

def temperature_converet_celsius_to_fahrenheit(temperature):
  return "{:.2f}".format(temperature * 1.8 + 32)

def temperature_Converet_Fahrenheit_To_Celsius(temperature):
  return "{:.2f}".format((temperature - 32 ) * (5 / 9))

def temperatureConveretCelsiusToKelvin(temperature):
  return "{:.2f}".format(temperature + 273.15)

def temperatureConveretKelvinToCelsius(temperature):
  return "{:.2f}".format(temperature - 273.15)

def temperatureConveretFahrenheitToKelvin(temperature):
  return "{:.2f}".format((temperature - 32) * (5 / 9) + 273.15)

def temperatureConveretKelvinToFahrenheit(temperature):
  return "{:.2f}".format((temperature - 273.15) * (9 / 5) + 32)


temperature = float(input("Digite a temperatura em Celsius: "))
control = ""

def temperature_converet_celsius_to_fahrenheit(temperature):
  return "{:.2f}".format(temperature * 1.8 + 32)

def temperature_converet_fahrenheit_to_celsius(temperature):
  return "{:.2f}".format((temperature - 32 ) * (5 / 9))

def temperature__Converet_Celsius_To_Kelvin(temperature):
  return "{:.2f}".format(temperature + 273.15)

def temperature_ConveretKelvinToCelsius(temperature):
  return "{:.2f}".format(temperature - 273.15)

def temperature_ConveretFahrenheitToKelvin(temperature):
  return "{:.2f}".format((temperature - 32) * (5 / 9) + 273.15)

def temperature_ConveretKelvinToFahrenheit(temperature):
  return "{:.2f}".format((temperature - 273.15) * (9 / 5) + 32)


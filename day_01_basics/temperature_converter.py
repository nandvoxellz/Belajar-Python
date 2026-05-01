# KONSTANTA
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

# Input User
celcius_input = 20
fahrenheit_input = 85

# Proses Konversi
converted_to_fahrenheit = (celcius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_celsius = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Output Hasil
print(f"{celcius_input}°C is equal to {converted_to_fahrenheit:.2f}°F")
print(f"{fahrenheit_input}°F is equal to {converted_to_celsius:.2f}°C")
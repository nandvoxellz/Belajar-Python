# KONSTANTA
MILE_TO_KILOMETER = 1.60934
KILOMETER_TO_MILE = 1 / MILE_TO_KILOMETER

# Input User
miles_input = 5
kilometers_input = 8

# Proses Konversi
converted_to_kilometers = miles_input * MILE_TO_KILOMETER
converted_to_miles = kilometers_input * KILOMETER_TO_MILE

# Output Hasil
print(f"{miles_input} miles is equal to {converted_to_kilometers:.2f} kilometers")
print(f"{kilometers_input} kilometers is equal to {converted_to_miles:.2f} miles")
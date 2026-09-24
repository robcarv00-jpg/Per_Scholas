import numpy as np


# Suppose you have a year's worth of daily temperature data in Celsius
temperature_data = np.array([
	22.3, 23.1, 24.5, 25.8, 23.6, 26.7, 27.9, 29.2, 30.5, 24.7,
	23.4, 22.1, 25.3, 26.4, 28.7, 29.8, 31.2, 32.4, 30.7, 29.5,
	27.8, 26.6, 23.9, 22.5, 24.1, 25.7, 27.3, 29.6, 31.0, 33.1, 31.9
])

# Calculate the mean, median, and standard deviation
mean_temperature = np.mean(temperature_data)
median_temperature = np.median(temperature_data)
standard_deviation = np.std(temperature_data)

# Print mean, median, and standard deviation in an organized manner
print(f"Mean temperature: {mean_temperature:.2f}°C")
print(f"Median temperature: {median_temperature:.2f}°C")
print(f"Standard deviation: {standard_deviation:.2f}°C")

# Find and count days with temperatures above 30°C
hot_days = temperature_data[temperature_data > 30]
hot_day_count = len(hot_days)

print(f"Hot days (>30°C): {hot_days}")
print(f"Number of hot days: {hot_day_count}")

# Convert all temperatures to Fahrenheit
temperature_fahrenheit = (temperature_data * 9 / 5) + 32

print(f"Temperatures in Fahrenheit: {temperature_fahrenheit}")

## BONUS ##
# Calculate total cooling degree days using a base temperature of 20°C.
base_temperature = 20
cooling_degree_days = np.sum(np.maximum(temperature_data - base_temperature, 0))

print(f"Total cooling degree days: {cooling_degree_days:.2f}")

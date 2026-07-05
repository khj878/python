import math

average_temperature_yesterday = 36.5
average_temperature_today = 36.4
standard_difference = 0.1

temperature_difference = average_temperature_yesterday - average_temperature_today
is_close_to_standard = math.isclose(temperature_difference, standard_difference)

print(f"온도 차이: {temperature_difference}")
print(f"0.1과 가까운가?: {is_close_to_standard}")

from datetime import datetime

expected_date = "2024-09-26"

formatted_date = datetime.strptime(expected_date,"%Y-%m-%d")
expected_day = formatted_date.day
expected_month = formatted_date.month
expected_year = formatted_date.year

print(expected_year)
print(expected_day)
print(expected_month)
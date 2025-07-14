total_seconds = int(input("Please enter an integer from 0 to 8640000: "))

days = total_seconds // 86400
remaining = total_seconds % 8640000
hours = remaining // 3600
remaining %= 3600
minutes = remaining // 60
seconds = remaining % 60

if days == 1:
    day_word = "day"
else:
    day_word = "days"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

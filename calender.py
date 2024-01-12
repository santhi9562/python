import calendar

# Get the year and month from the user
year = int(input("Enter the year: "))
month1 = int(input("Enter the month (1-12): "))

# Validate input
if 1 <= month1 <= 12:
    # Print the calendar
    cal = calendar.month(year, month1)
    print(f"\nCalendar for {calendar.month_name[month1]} {year}:\n")
    print(cal)
else:
    print("Invalid month. Please enter a month between 1 and 12.")

# Input: Enter a year
year = int(input("Enter a year: "))

# Logic to check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} đây là năm nhuận  .")
else:
    print(f"{year} đây ko phải là năm nhuận đâu .")

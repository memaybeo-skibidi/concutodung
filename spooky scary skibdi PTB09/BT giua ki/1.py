from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Input: Prompt the user for their year of birth
year_of_birth = int(input("Nhập năm sinh của bạn đi skibidi: "))

# Calculate the age
age = current_year - year_of_birth

# Output: Display the user's age
print(f"Bạn {age} tuổi.")

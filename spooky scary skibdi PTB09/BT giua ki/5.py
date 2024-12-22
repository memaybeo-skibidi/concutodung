def calculate_ticket_price(age):
    """
    Calculate the ticket price based on age.

    :param age: int - The age of the person
    :return: int - Ticket price in VND
    """
    if age < 12:
        return 50000  # Children under 12
    elif 12 <= age <= 60:
        return 100000  # Adults between 12 and 60
    else:
        return 70000  # Seniors above 60

# Input: Ask the user for their age
try:
    age = int(input("Nhập tuổi của bạn: "))
    if age < 0:
        print("Tuổi đéo hợp lệ .")
    else:
        # Calculate ticket price
        price = calculate_ticket_price(age)
        # Output: Display the ticket price
        print(f"Giá vé của tuổi {age} là: {price:,} VND")
except ValueError:
    print("ĐKo hợp tuổi nhập lại đi.")

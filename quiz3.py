phone_number = input("Enter a phone number:")
if phone_number.startswith("+254"):
    print("Phone number is already in the correct format.")
else:
    if phone_number.startswith("07"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("71"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("254"):
        phone_number = "+254" + phone_number[3:]
    elif phone_number.startswith("01"):
        phone_number = "+254" + phone_number[1:]
    else:
        print("Invalid phone number format.")
        exit()

    print("Converted phone number:", phone_number)


def validate_email(email):
    if "@" in email and "." in email:
        valid_email = True
    else:
        valid_email = False

    if valid_email:
        print("Valid email address")
    else:
        print("Invalid email address")


email = input("Enter an email address: ")

validate_email(email)

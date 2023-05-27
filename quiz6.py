password = "admin@123"
attempts = 4
while attempts > 0:
    user_passcode = input("Enter the password:")
    if user_passcode == password:
        print("Access grandted.")
        break
    else:
        attempts-=1
        print("Incorrect password.Attempts left:",attempts)
        if attempts == 0:
            print("Account blocked.")

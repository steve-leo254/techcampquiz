attempts = 3
while attempts > 0:
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is Successful")
        break
    else:
        attempts -= 1
        print("Invalid username or password. Attempts remaining:", attempts)

if attempts == 0:
    print("You have been blocked.")
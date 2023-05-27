import datetime
dob = input("Enter the date of birth (YYYY-MM-DD): ")
current_date = datetime.date.today()
dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
age = current_date - dob_date
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30
print("Age: {} years, {} months, {} days".format(years, months, days))

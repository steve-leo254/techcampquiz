#Write a program that takes input of someone's 
#basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF
# Define the NHIF rate thresholds and corresponding deductions
def calculate_nhif(gross_salary):
    if gross_salary < 6000:
        nhif_contribution = 150
    elif gross_salary < 8000:
        nhif_contribution = 300
    elif gross_salary < 12000:
        nhif_contribution = 400
    elif gross_salary < 15000:
        nhif_contribution = 500
    elif gross_salary < 20000:
        nhif_contribution = 600
    elif gross_salary < 25000:
        nhif_contribution = 750
    elif gross_salary < 30000:
        nhif_contribution = 850
    elif gross_salary < 35000:
        nhif_contribution = 900
    elif gross_salary < 40000:
        nhif_contribution = 950
    elif gross_salary < 45000:
        nhif_contribution = 1000
    else:
        nhif_contribution = 1100

    return nhif_contribution

basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the benefits: "))

gross_salary = basic_salary + benefits


nhif = calculate_nhif(gross_salary)

print("Gross Salary: ", gross_salary)
print("NHIF Contribution: ", nhif)


marks = int(input("Enter student marks (between 0 and 100): "))

if marks > 100 or marks < 0:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks > 79:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: E")

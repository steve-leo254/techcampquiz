speedkms = float(input("Enter the cars's speed:"))
if speedkms <70:
    print("Ok")
else:
    demerit_points=(speedkms-70)//5
    if demerit_points >12:
        print("License suspended")
    else:
        print("License suspended")
import re
def input():
    a=int(input("Enter the phone number: ")) 
    b=int(input("Enter the Email.id: "))
    phone_pattern =r'^\d{10}$'
    email_pattern =r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(phone_pattern, str(a)):
        print("Valid phone number")
    else:
        print("Invalid phone number")
    if re.match(email_pattern, str(b)):
        print("Valid email id")
    else:
        print("Invalid email id")
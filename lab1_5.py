#Test 1

def check_multiple(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False

#Test 2

def check_password(password):
    if password == "Python123":
        return "access granted"
    else: 
        return "access denied"

#Test 3

def calculate_federal_tax(salary):
    if salary <= 10000:
        return salary * 0.10
    elif salary <= 50000:
        return salary * 0.22
    else:
        return salary * 0.24
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to the tip calculator!")
... bill = float(input("What was the total bill? "))
... tip = int(input("How much percent tip would you like to give? "))
... people = int(input("How many people to split the bill?"))
... 
... 
... tip_percent=bill*(tip/100) 
... total_bill=tip_percent+bill
... bill_per_person = total_bill / people
... final_amount = round(bill_per_person, 2)
... 
... 
... print(f"Each person should pay: {final_amount}")
SyntaxError: multiple statements found while compiling a single statement

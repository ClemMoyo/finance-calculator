
# program to calculate investment future value and mortgage repayment
import math
# prompt the user to input a menu option
user_input = ''
line = "x" 
print(line * 100)
menu = """1:Investment - To calculate the amount of interest you 'ill earn on your investment
2:Bond - To calculate the amount you 'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: 
"""
user_input = input(menu).casefold() # force change user input characters to lower case
p = 0
t = 0
r = 0
i = 0
n = 0
# calculation for investment option
if user_input == "investment":  
    p = int(input("Please enter amount you want to invest: "))
    print("You want to deposit:", p)
    t = int(input("Please enter years you want to invest between 1 and 25: "))
    r  = int(input("Plaese enter 8 for annual interest: " ))
# interest option input by user
    menu_int = """Please select interest option below:
    1: Option 1 - simple interest
    2: Option 2 = compound interest """

    user_int = ""
    r = r / 100
    fv = p * ( 1 + ( t * r))
    a = p * math.pow((1+r), t)
    user_int = input(menu_int)
    if user_int == "1": 
        print("You selected simple interest. Your investment total:", fv)
    elif user_int == "2":
            print("Your compounded investment total is:", a)
    elif user_int != "1" or "2":
        print("Choose interest option to proceed", menu_int)
    else:
        print("refresh page and select your option to proceed")       
#calculation of mortgage monthly repayment
elif user_input == "bond":
    print("Mortgage calculation option selected.")
    p = int(input("Please enter current value of house: "))
    n = int(input("Please enter time you plan to repay the mortgage in months: "))
    i = int(input("Please enter 5 for interest: "))
    i= i / 100
    repayment = (i* p )/(1-(1+i)**(-n))
    print("Your monthly repayment is", repayment)
while user_input != "investment" or "bond":
    print( menu)
    break
else:   
    print("Please refresh page and make a selection")

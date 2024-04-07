
# program to calculate investment future value and mortgage repayment
import math

def calculate_investment():
    print("Investment calculation option selected.")
    principal = float(input("Please enter the amount you want to invest: "))
    years = int(input("Please enter the number of years you want to invest between 1 and 25: "))
    interest_rate = float(input("Please enter the annual interest rate (in percentage): ")) / 100
    
    menu_int = """Please select interest option below and enter 1 or 2:
    Option 1 - Simple interest
    Option 2 - Compound interest
    """
    user_int = input(menu_int)
    
    if user_int == "1":
        simple_interest = principal * (1 + years * interest_rate)
        print("Your simple interest total is:", round(simple_interest))
    elif user_int == "2":
        compound_interest = principal * math.pow((1 + interest_rate), years)
        print("Your compounded interest total is:", round(compound_interest, 2))
    else:
        print("Invalid option. Please select a valid interest option.")

def calculate_bond():
    print("Mortgage calculation option selected.")
    house_value = float(input("Please enter the current value of the house: "))
    months = int(input("Please enter the time you plan to repay the mortgage in months: "))
    interest_rate = float(input("Please enter the annual interest rate (in percentage): ")) / 100
    
    monthly_interest_rate = interest_rate / 12
    monthly_repayment = (monthly_interest_rate * house_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    
    print("Your monthly repayment is:", round(monthly_repayment, 2))

def main():
    print("# Program to calculate investment future value and mortgage repayment")
    print("#" * 100)
    
    while True:
        menu = """     
        Choose an option from below\n
        1: Investment: To calculate the amount of interest you'll earn on your investment
        2: Bond:       To calculate the amount you'll have to pay on a home loan\n
        Enter either 'investment' or 'bond' from the menu above to proceed:      """
        user_input = input(menu).strip().lower()
        
        if user_input == "investment":
            calculate_investment()
            break
        elif user_input == "bond":
            calculate_bond()
            break
        else:
            print("Invalid option. Please select 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
   
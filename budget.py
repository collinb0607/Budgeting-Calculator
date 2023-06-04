# Simple Budgeting Calculator
# Collin Brooks (collinbrooks.com)
# 6/2/23 
# Description: This program will provide a sample monthly budget given an income in the state of NJ.
#              It can be given an hourly wage with a number of hours worked per week or an annual salary.
#              The program will provide spending habits for rent, investments, savings, necessities, and nonessentials (wants).
#              In addition, it handles any kind of input without crashing, and can be done infinitely, until "q" is typed to quit.

rent = necessities = spending = savings = investments = net_annual_inc = inc = annual_taxes = state_taxes = fed_taxes = total_taxes = 0.0

def calc_budget(annual_inc):
    global rent, necessities, spending, savings, investments, net_annual_inc, inc, annual_taxes, state_taxes, fed_taxes, total_taxes
    fed_taxes = calc_fed_taxes(annual_inc)
    state_taxes = calc_state_taxes(annual_inc)
    annual_taxes = fed_taxes + state_taxes
    net_annual_inc = annual_inc - annual_taxes
    inc = net_annual_inc/12.00 # Net Monthly Income
    fed_taxes /= 12.00 # Monthly Fed Taxes
    state_taxes /= 12.00 # Monthly State Taxes
    total_taxes = fed_taxes + state_taxes # Total Monthly Taxes
    rent = (annual_inc/12) * 0.30 # Rent should be 30% of GROSS income, not net
    necessities = inc * 0.20
    savings = inc * 0.05
    investments = inc * 0.15
    spending = inc - (rent + necessities + savings + investments)

def print_budget(annual_income):
    temp = int(annual_income)
    format = len(str(temp)) # Format will leave just enough space for your specific income
    format += 3.2
    global rent, necessities, spending, savings, investments, net_annual_inc, inc, annual_taxes, state_taxes, fed_taxes, total_taxes
    print('Annual Gross Income: \t\t$','{:{}f}'.format(annual_income, format))
    print('Annual Net Income: \t\t$','{:{}f}'.format(net_annual_inc, format))
    print('Annual Taxes: \t\t\t$','{:{}f}'.format(annual_taxes, format))
    print('Monthly Net Income: \t\t$','{:{}f}'.format(inc, format))
    print('Federal Taxes Part Monthly: \t$','{:{}f}'.format(fed_taxes, format))
    print('State Taxes Part Monthly: \t$','{:{}f}'.format(state_taxes, format))
    print("")
    print(f'This is the suggested amount you should be paying for each item monthly:')
    print('Rent: \t\t\t\t$','{:{}f}'.format(rent, format))
    print('Other Necessities: \t\t$','{:{}f}'.format(necessities, format))
    print('Spending Money: \t\t$','{:{}f}'.format(spending, format))
    print('Reliable Savings Account: \t$','{:{}f}'.format(savings, format))
    print('Reliable Investment Account: \t$','{:{}f}'.format(investments, format))
    print("\n\n")

def calc_fed_taxes(annual_inc) -> float:
    if(annual_inc <= 10275):
        return annual_inc*.10
    elif(annual_inc <= 41775):
        return (annual_inc-10275) * 0.12 + 1027.50
    elif(annual_inc <= 89075):
        return (annual_inc-41775) * 0.22 + 4807.50
    elif(annual_inc <= 170050):
        return (annual_inc-89075) * 0.24 + 15213.50
    elif(annual_inc <= 215950):
        return (annual_inc-170050) * 0.32 + 34647.50
    elif(annual_inc <= 539900):
        return (annual_inc-215950) * 0.35 + 49335.50
    else:
        return (annual_inc-539900) * 0.37 + 162718.00
    
def calc_state_taxes(annual_inc) -> float: # According to NJ Income Tax
    if(annual_inc <= 20000):
        return annual_inc*.014
    elif(annual_inc <= 35000):
        taxes = (annual_inc-20000) * 0.0175 + 280.00
        return taxes
    elif(annual_inc <= 40000):
        taxes = (annual_inc-35000) * 0.035 + 542.50
        return taxes
    elif(annual_inc <= 75000):
        taxes = (annual_inc-40000) * 0.05525 + 717.50
        return taxes
    elif(annual_inc <= 500000):
        taxes = (annual_inc-75000) * 0.0637 + 2651.25
        return taxes
    elif(annual_inc <= 1000000):
        taxes = (annual_inc-500000) * 0.0897 + 29723.75
        return taxes
    else:
        taxes = (annual_inc-1000000) * 0.1075 + 74573.75
        return taxes
    
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def main():
    print("-------------------------------------------------------------------------------------")
    print("This calculator will calculate your net income and recommend spending budgets per month.")
    print("This is to be used as an estimation only and not as financial advice.")
    print("State Tax is calculated based on NJ Income Tax\n")
    wage = input("First, I need to know if this your hourly wage or annual salary? (h or s, q to quit): ")
    while wage == "s" or wage == "h":
        if wage == "h":
            annual_income = input("Please enter your hourly rate: $")
            if is_float(annual_income):
                annual_income = float(annual_income)
                hours = input("How many hours per week do you work?: ")
                annual_income = 52.14 * float(hours) * annual_income
                calc_budget(annual_income)
                print_budget(annual_income)
        else:
            annual_income = input("Please enter your annual income: $")
            if is_float(annual_income):
                annual_income = float(annual_income)
                calc_budget(annual_income)
                print_budget(annual_income)
        wage = input("First, I need to know if this your hourly wage or annual salary? (h or s, q to quit): ")
main() 
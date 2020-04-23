#a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
import math
product = input ('''Choose either 'investment' or 'bond' from the menu below to proceed:\n 
                 investment  - to calculate the amount of interest you'll earn on interest\n
                 bond        - to calculate amount you'll have to pay on a home loan:\n''')


if product ==  "investment" or product ==  "Investment" or product ==  "INVESTMENT":
    #the amount that the user deposits.
    P = float(input ('Enter the amount of money to be deposited: '))
    int_rate = float (input('Enter interest rate: '))
    #below is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
    r = int_rate/100
    #is the number of years that the money is being invested for.
    t = int (input('Enter the number of years you plan on investing for: '))
    interest = input ('Choose if you want "simple" or "compound" interest')
    #varables that store investment calculation

    if interest == "simple":
        simple_interest = P*(1 + r * t)
        print ('The expected amount after', t, 'years is', simple_interest)


    elif interest == "compound":
        compound_interest = P* math.pow((1+r),t)
        print ('The expected amount after', t, 'years is', compound_interest)


elif product == "bond" or product == "Bond" or product ==  "BOND":
    #is the present value of the house
    PV = float (input(' Enter the present value of the house: '))
    #is the interest rate per period.
    int_rate = int(input('Enter the interest rate:'))
    #is the interest rate per month
    r = int_rate/12 
    #the number of months over which the bond will be repaid.
    n = int (input('Enter The number of months you plan to take to repay the bond:  '))
    #important note**the given bond formular in the project book is not right or accurate
    bond = PV/((1 - (1-(r/100))**-n )/r)
    print( 'Your monthly repayment will be', bond)
      
else:
    print('Your input is not valid, please try again by choosing appropriate option "investment" or bond')
    

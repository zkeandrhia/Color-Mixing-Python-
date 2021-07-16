def ci():
    p = float(input('Amount deposited: '))
    r = float(input('Annual interest rate paid by the account: '))
    n = float(input('Number of times per year that the interest is compounded(For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4): '))
    t = float(input('Number of years the account will be left to earn interest:'))

    A= p * (pow((1 + r / 100), t))
    ci = A - p
    print(f'Amount of money that will be in the account after the specified number of years: {ci}')
    
ci()

# Get loan info
money_owed = float(input('Amount owed:\n'))
apr = float(input('APR %:\n'))
payment = float(input('Monthly payment:\n'))
months = int(input('Number of months:\n'))

monthly_rate = apr/100/12

for m in range(months):
    int_paid = money_owed*monthly_rate
    money_owed = money_owed + int_paid
    if (money_owed - payment < 0):
        print('The last payment was', money_owed)
        print('You paid off the loan in', m+1, 'months')
        break
    money_owed = money_owed - payment
    print('Paid', payment, 'of which', int_paid, 'was interest', end=' ')
    print('Now you owe', money_owed)

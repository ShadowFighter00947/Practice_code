empID = input('Enter your employee ID:- ')
while (empID != '-1'):
    trade = int(input('Enter your trade amount:- '))
    profit_loss = 0
    while (trade != 0 ):
        profit_loss = profit_loss + trade
        trade = int(input('Enter your trade amount:- '))
    print('Your profit/loss is {0}'.format(profit_loss))
    empID = input('Enter your next employee ID:- ')
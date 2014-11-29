def shopping_budget(gift_card, cash):  # define function and create arg or parameters- gift card and cash
    print "You have %r on your gift card" % gift_card  # create variables for giftcard
    print "You have %r on cash" % cash  # create variable for cash
    print "Let's go shopping"

shopping_budget(45, 76.50)  # replace arguments with numbers

total = 45 + 76.50  # create a new variable using above numbers

print "You have %r to spend" % total  # print statement of totals

purchase = raw_input("how much did you spend on a shirt?")  # ask user for input
print purchase  # prints user input
print "you spent $", purchase, "of your budget"
budget_left = float(total) - float(purchase)  # create variable to calculate total and purchase
#print budget_left
print "Now you have $", budget_left, "left"  # prints users balance

# def cash_or_card():
#     print raw_input("was the $%s cash or card? " % purchase),
#     if raw_input == card:
#         print "your card balance is", gift_card - purchase,

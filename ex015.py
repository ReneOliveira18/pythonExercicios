days = int(input('How many days do you want to rent the car for?'))
km = float(input('How many km have you driven?'))
price = (days * 60) + (0.15 * km)
print('You rented the car for {} days and drove {}km, \nthe total amount to pay is ${:.2f}'.format(days, km, price))
value = float(input('What is the value of the product?$'))
disc = value - (value * 0.05)
print('The value of the product is ${:.2f} with the 5% discount it was ${:.2f}'.format(value, disc))

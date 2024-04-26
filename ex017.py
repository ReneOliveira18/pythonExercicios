import math
oppside = float(input('What is the opposite side? '))
adjside = float(input('What is the adjacent side? '))

#hypot = math.sqrt(oppside*oppside + adjside*adjside)
hypot = math.hypot(oppside, adjside)

print('Opposite side {} and Adjacent side {} = {:.2f} hypotenuse.'.format(oppside, adjside, hypot))

b = float(input('Enter the widht of the wall in meters: '))
h = float(input('Enter the height of the wall in meters: '))
area = b * h
paintcans = area/2
print('You want to paint a wall of {:.2f}m², \nyou will need {:.2f}l cans of paint'.format(area, paintcans ))

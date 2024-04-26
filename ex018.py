import math
#from math import radians, sin, cos, tan

ang = float(input('Enter an angle to calculate sin, cos, tangent: '))
rad = math.radians(ang)

cos = math.cos(rad)
sin = math.sin(rad)
tan = math.tan(rad)

print('The angle {}º has \ncos {:.3f} \nsin {:.3f} \ntang {:.3f}'.format(ang, cos, sin, tan))


#import random
from random import choice
stud = input('Enter the name of the first student:')
stud1 = input('Enter the name of the second student:')
stud2 = input('Enter the name of the third student:')
stud3 = input('Enter the name of the fourth student:')
list = [stud, stud1, stud2, stud3]
print('Among these students,{}, {}, {} e {} \nthe chosen one was: {}. '.format(stud, stud1, stud2, stud3, choice(list)))

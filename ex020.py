from random import shuffle

stud = input('Enter the name of the first student:')
stud1 = input('Enter the name of the second student:')
stud2 = input('Enter the name of the third student:')
stud3 = input('Enter the name of the fourth student:')
list = [stud, stud1, stud2, stud3]

shuffle(list)

print('The order of presentation of the work is:')
print(list)
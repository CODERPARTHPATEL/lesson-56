# program to check if user input numbers are equal

def checkifsame(number1, number2):

#using XQR oporator as a^a is always 0
    if((number1 ^ number2)!= 0):
        print('number are not equal')
    else:
        print('both numbers are equal')
        # taking input
number1 = int(input('enter first number to compare'))
number2 = int(input('enter second number to compare'))

checkifsame(number1, number2)
# from example import b

# print(b)


# from mypackage.functions import add, average, power

# print(add(4, 11))

# from mypackage.greet import SayHello

# SayHello('Abdulla') 

# import this
# import codecs

# z = codecs.decode(this.s, 'rot_13')

# with open('zen_of_python.txt', 'w') as test:
#     test.write(z)


# # generate numbers from 1 to 50
# # if number is divisible by 3 and 5, print Hello world
# # if number is divisible by 3, print hello
# # if number is divisible by 5, print world
# # if it's not divisible, show number itself


# for number in range(1, 51):
#     if number % 3 == 0 and number % 5 == 0:
#         print('Hello world')
#     elif number % 3 == 0:
#         print('Hello')
#     elif number % 5 == 0:
#         print('World')
#     else:
#         print(number)


def check_evenness(number:int):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(check_evenness(0))


# bank account
# account = 0
# deposit = account +=any deposit
# withdrawal = account -=any withdrawal (if withdrawal money > account, then print 'not enough money in balance')
# check_balance = need to check money inside of account


# create a function that will find sum of digits I provide (use for loop)
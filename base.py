# Q1
# Find a max number from a given random number list

# from random import randint

# def makelist(count):
#     return [randint(1,100) for i in range(count)]

# def actual_list():
#     a = randint(6,12)
#     # print(a)
#     nums = makelist(a)
#     # print(nums)
#     return nums

# def max_value():
#     nums = actual_list()
#     max = nums[0]
#     for i in range(len(nums)):
#         if max < nums[i]:
#             max = nums[i]
#     print(f" The list is {nums}.")
#     print(f" The max value in the list is {max}.")

# max_value()

# Q2
# #is prime
'''Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.'''

from random import randint
from math import *

def is_prime(a):
    cnt = 0
    if a < 2:
        print(f"The number is {a}. It is not a prime number.")
    
    for i in range(2, floor(sqrt(a)) + 1):
        if (a % i == 0):
            cnt = cnt + 1
        if cnt > 0:
            break
    
    if cnt == 0:
        print(f"The number is {a}. It is a prime number.")
    else:
        print(f"The number is {a}. It is not a prime number.")



a = randint(0,1000)
is_prime(a)
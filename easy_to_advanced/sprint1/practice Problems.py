

"""Odd Even Numbers"""
""" Write a program to check if a number is odd or even"""



def odd_even(num):

    if num %2 == 0:
        return "Even"
    else:
        return "Odd"

res = odd_even(5)


"""Prime Numbers"""
"Check if a number is prime or not"

def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

res = is_prime(6)
# print(res)


"""Validating Leap Year"""
"""Check if an year is a leap year or not"""

def leap_year(year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"

res = leap_year(1998)
# print(res)


"""Calculating Armstrong Numbers"""

def checkAmstrong(num):

    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        return True
    else:
        return False

res = checkAmstrong(153)

# print(res)

"""Fibonaci Series"""

def fibonacci_series(num):

    if num <= 1:
        return 1
    return fibonacci_series(num-1) + fibonacci_series(num-2)

res = fibonacci_series(5)
# print(res)


"""Identifying Palindromes"""

def palindromes(word):

    # Go till half of the word, while comparing the first and last character of the word
    for i in range(0, len(word)//2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
    #
    # if word[::-1] == word:
    #     return True
    # else:
    #     return False

res = palindromes("abcba")
# print(res)
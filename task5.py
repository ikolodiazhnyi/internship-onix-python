from datetime import datetime
from datetime import timedelta
import random
import string

date_tomorrow = datetime.today() + timedelta(days=1)
date_tomorrow = datetime.strftime(date_tomorrow, '%d-%m-%Y %H:%S')
print(date_tomorrow)

var_date = '2020-02-03 09:18:36.000'
var_date = datetime.strptime(var_date, '%Y-%m-%d  %H:%M:%S.%f')
print(var_date.strftime('%d\n%m\n%Y\n%H\n%S'))


def get_three():
    """ Get three random numbers which divide by five """
    three_nums = []

    while len(three_nums) != 3:
        # randrange doesn’t consider the last item i.e. it is exclusive.
        rand_num = random.randrange(100, 1000)
        if rand_num % 5 == 0:
            three_nums.append(rand_num)

    return three_nums


print(get_three.__doc__, get_three())


def get_rand_str(str_len=10):
    """ Get a string out of the random letters """
    letters = string.ascii_letters
    rand_list = random.sample(letters, str_len)

    return "".join(rand_list)


print(get_rand_str.__doc__, get_rand_str())


def get_rand_list(list_len=100):
    """ Get a list with 100 nums, each num is out of 10 digits """
    digits = string.digits
    rand_list = []

    for i in range(list_len):
        num = "".join(random.sample(digits, 10))
        rand_list.append(num)

    return rand_list


tickets = get_rand_list()
winning_tickets = random.sample(tickets, 2)
print(winning_tickets)


def exception_trainee():
    try:
        num = float(input("Enter a numeric variable: "))
    except ValueError:
        print("Please, enter a numeric variable :(")
    except Exception:
        print("The unknown error was occurred :|")
    else:
        print("Well done! :) You entered:", num)
    finally:
        print("Finally...")


exception_trainee()

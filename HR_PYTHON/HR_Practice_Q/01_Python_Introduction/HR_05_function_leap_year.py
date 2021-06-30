
"""
1. The year can be evenly divided by 4, is a leap year, unless:

2. The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.

Logic: If it is divisible by 4 then it is a leap year and shouldn't be divisible by 100.
       If it is divisible by 4 and also divisible by 100 then it has to be divisible by 400

"""


#   1.
def is_leap(year: int) -> bool:
    """
    1. If div by 4 check for div by 100.
    2. If div by 4 and 100 then check with 400
    3. Leap year
    4. else Not a Leap year

    :param year:
    :return: True or False
    """

    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
        # Write your logic here

    return leap


# ##################################################################################

#   2.
def is_leap_using_logical_op(year):
    """
    1. If div by 4 and not div by 100 --> Leap
    2. If 1 is false then div by 400 --> Leap
    """

    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True

    return leap


# ######################################################################################

#   3.
def reverse_checking_leap(year):
    """
    1. If div by 400 then leap
    2. if not div by 100 check with 4 then leap
    """

    if year % 400 == 0:
        return True
    elif year % 100 != 0:
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        return False


# #####################################################################################

#   4.

def check_leap_using_built_in_module(year):
    import calendar
    return calendar.isleap(year)


if __name__ == "__main__":
    y = int(input())
    print(check_leap_using_built_in_module(y))


# Sample Input - 2100 -> F
#                2000 -> T
#                2020 -> T


"""
    Task
    Given an integer, n, perform the following conditional actions:

       ● If n is odd, print Weird
       ● If n is even and in the inclusive range of 2 to 5, print Not Weird
       ● If n is even and in the inclusive range of 6 to 20, print Weird
       ● If n is even and greater than 20, print Not Weird
"""


# Here 0 input will have no O/p. Debug to understand.
def wrong_code(n):
    if n % 2 == 0:
        if n in range(2, 6):     # if 2 <= n < 6:
            print("Not Weird")

        elif n in range(6, 21):
            print("Weird")

        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")


# In the below function 0 input will have o/p as value out of range
def right_code(n):
    if n % 2 == 1:
        print("Weird")

    elif n % 2 == 0 and (2 <= n < 6):  # simplified chained comparison
        print("Not Weird")

    elif n % 2 == 0 and (6 < n < 21):  # # simplified chained comparison
        print("Weird")

    elif n % 2 == 0 and n > 20:
        print("Not Weird")

    else:
        print("Value out of range")


if __name__ == '__main__':

    user_input = int(input("Please Enter a number: ").strip())
    right_code(user_input)      # right answer
    wrong_code(user_input)

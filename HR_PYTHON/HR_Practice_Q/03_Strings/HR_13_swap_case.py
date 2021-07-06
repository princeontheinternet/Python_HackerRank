
"""
You are given a string and your task is to swap cases.
    In other words, convert all lowercase letters to uppercase letters and vice versa.

Sample Input:
    HackerRank.com presents "Pythonist 2".
Sample Output:
    hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(sentence):

    t = ''
    for i in sentence:
        if i.isupper():
            t += i.lower()
        elif i.islower():
            t += i.upper()
        else:
            t += i
    return t


def another_way(sentence):
    return sentence.swapcase()


if __name__ == '__main__':
    s = input()
    print(swap_case(s))
    print(another_way(s))

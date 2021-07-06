
"""
Without using any string methods, try to print the following:
123...n

Example:
n=5
Print the string 12345.
"""


if __name__ == '__main__':
    n = int(input())

    # for i in range(n):
    #     print(i + 1, sep='', end='')

    list1 = [i+1 for i in range(n)]
    print(*list1, sep='')

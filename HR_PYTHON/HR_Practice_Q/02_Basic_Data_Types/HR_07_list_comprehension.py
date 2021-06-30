# List Comprehensions

"""
    You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
    Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

Sample Input:
x = 1
y = 1
z = 1
n = 2

Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    final_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

    print(final_list)

    # Without list comprehension, debug this to get more clarity

    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # final_list =[]
    # for i in range(1+x):
    #     for j in range(y+1):
    #         for k in range(1+z):
    #             if i+j+k!=n:
    #                 temp=[i,j,k]
    #                 final_list.append(temp)
    #             else:
    #                 continue
    # print(final_list)

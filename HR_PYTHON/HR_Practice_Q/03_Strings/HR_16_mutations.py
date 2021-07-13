
"""
Problem:
    Read a given string, change the character at a given index and then print the modified string.


Sample Input:
    abracadabra
    5 k         # 5 is position and k is the character

Sample Output:
    abrackdabra
"""


# Changing the string using list
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)


# Changing the string using slicing the string
def mutate_string_using_slicing(string, position, character):
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()  # i is the index, c is the char which needs to be replaced.
    s_new = mutate_string(s, int(i), c)
    print(s_new)

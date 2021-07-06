# Find the Runner-Up Score!

"""
Sample Input:
5
2 3 6 6 5
Sample Output:
5
"""


def using_len_sorted_list_set(user_array):
    list(user_array)

    sorted_distinct_list = sorted(list(set(user_array)))
    total_len = len(sorted_distinct_list)
    runner_up_score = sorted_distinct_list[total_len - 2]
    return runner_up_score


def using_sorted_reverse_list_set(user_array):
    runner_up_score = sorted(list(set(user_array)), reverse=True)[1]  # Optional: use set, remove list after sort
    return runner_up_score


def removing_max(user_array):
    max_value = max(user_array)

    while True:
        if max_value == max(user_array):
            user_array.remove(max(user_array))
        else:
            break

    return max(user_array)


if __name__ == '__main__':
    n = int(input())
    arr = (map(int, input().split()))
    list_arr = list(arr)

    # 1.
    print(using_len_sorted_list_set(list_arr))
    # 2.
    print(using_sorted_reverse_list_set(list_arr))
    # 3.
    print(removing_max(list_arr))

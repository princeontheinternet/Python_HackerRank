if __name__ == '__main__':
    N = int(input())
    sample_list = []

    for i in range(N):
        cmd = input().strip().split()
        cmd_list = cmd[0]

        if cmd_list == 'append':
            sample_list.append(int(cmd[1]))

        elif cmd_list == 'insert':
            sample_list.insert(int(cmd[1]), int(cmd[2]))

        elif cmd_list == 'print':
            print(sample_list)

        elif cmd_list == 'remove':
            sample_list.remove(int(cmd[1]))

        elif cmd_list == 'pop':
            sample_list.pop()

        elif cmd_list == 'sort':
            sample_list.sort()

        elif cmd_list == 'reverse':
            sample_list.reverse()


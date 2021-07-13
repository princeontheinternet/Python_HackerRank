# HACKER RANK SAMPLE TEST FOR BASIC PYTHON CERTIFICATE

# Complete the 'fizzBuzz' function below.

# The function accepts INTEGER n as parameter.


def fizzBuzz(n):
    # Write your code here
    for x in ["FizzBuzz" if i % 5 == 0 and (i % 3 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i
              for i in range(1, n + 1)]:
        print(x)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

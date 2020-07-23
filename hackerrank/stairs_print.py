# Complete the staircase function below.
def staircase(n):
    count = 0
    space = n - 1
    for i in range(n):
        count += 1
        print(" " * space + "#" * count)
        space -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
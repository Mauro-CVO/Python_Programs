def run(arr):
    reverse = []
    i = len(arr) - 1
    for _ in range(len(arr)):
        reverse.append(str(arr[i]))
        i -= 1
    print(" ".join(reverse))
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    run(arr)
def Binary(n):
    binary = []
    count = 0
    while n != 0:
        biny = n % 2
        if biny == 1:
            count += 1
        else:
            count = 0
        n = n // 2
        binary.append(biny)

    binary = binary[::-1] #número en binario

    print(count)


def run():
    n = int(input())
    Binary(n)

if __name__ == '__main__':
    run()



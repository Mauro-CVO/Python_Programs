def run():
    count = 0
    count_ext = 0

    while count_ext < 5:
        while count < 6:
            print(count, count_ext)
            count += 1
            if count >= 3:
                break
            
        count_ext += 1
        count = 0

if __name__ == "__main__":
    run()
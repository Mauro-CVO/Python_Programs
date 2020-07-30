

def dictionary(phone_book, names):
    for name in names:
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found.")



def run():
    n = int(input())
    phone_book = {}
    names = []

    for i in range(n):
        entry = input("name y fon: ")
        print(entry)
        entry = entry.split()
        print(entry)
        phone_book.update({entry[0]:entry[1]})
    
    print(phone_book)

    for i in range(n):
        name = input("name: ")
        names.append(name)
    
    print(names)

    dictionary(phone_book, names)


if __name__ == "__main__":
    run()



# def run():
#     n = int(input())
#     name_numbers = [input().split() for _ in range(n)]
#     phone_book = {k: v for k,v in name_numbers}
#     while True:
#         try:
#             name = input()
#             if name in phone_book:
#                 print('%s=%s' % (name, phone_book[name]))
#             else:
#                 print('Not found')
#         except:
#             break
import random

def key_generator():
    mayus = ["A", "B", "C", "D", "E", "F", "G"]
    minus = ["a", "b", "c", "d" ,"e" ,"f" , "g"]
    num = ["#", "{", "|", "?", "¿", "~", "^", "+", "*"]
    sym =[ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    chars = mayus + minus + sym + num

    key = []

    for i in range(15):
        char_random = random.choice(chars)
        key.append(char_random)

    key = "".join(key)
    return key

def run():
    key = key_generator()
    print("Your new key is: " + key)

if __name__ == "__main__":
    run()
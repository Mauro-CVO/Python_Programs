def timeConversion(s):

    if s.endswith("PM"):
        s = s.replace("PM","").replace(":", " ").split()
        print(s)
        h = int(s[0]) + 12
        print(h)
        m = s[1]
        print(m)
        sec = s[2]
        print(sec)
        
    else:
        s = s.replace("AM","").replace(":", " ").split()
        h = int(s[0]) - 12
        m = s[1]
        sec = s[2]
        
    print(f"{h}:{m}:{sec}")

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
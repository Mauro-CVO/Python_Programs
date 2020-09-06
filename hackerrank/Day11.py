def hourglass(arr):
    res = []

    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            print(f"""
            
            {arr[x][y: y+3]}
            {arr[x+1][y+1]}
            {sum(arr[x+2][y: y+2])}
        
            """)
            res.append(s)

    print(max(res))

def run():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    hourglass(arr)



if __name__ == "__main__":
    run()
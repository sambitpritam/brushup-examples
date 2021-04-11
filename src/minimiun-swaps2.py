def min_swap():
    arr = [7,1,3,2,4,5,6]
    a = dict(enumerate(arr, 1))
    b = {v:k for k,v in a.items()}
    count = 0

    print(f"a: {a}")
    print(f'b: {b}')

    for i in a:
        x = a[i]
        if x != i:
            y = a[i]
            a[y] = x
            b[x] = y
            count += 1
        print(f"\nafter swap count: {count}")
        print(f"i: {i}, x=a[i]: {x}, y=a[i]: {y}, a[y]: {a[y]}, b[x]: {b[x]}")
        print(f"a: {a}")
        print(f"b: {b}")
    print(f'Total number of swaps required: {count}')

if __name__ == "__main__":
    min_swap()
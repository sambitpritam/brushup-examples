import time

def count_triplets(arr, const):
    result = 0

    right_dict = dict()
    left_dict = dict()

    for item in arr:
        right_dict[item] = right_dict.get(item, 0) + 1

    for i in arr:
        left_val = i//const
        right_val = i * const

        right_dict[i] = right_dict.get(i,0) - 1

        if left_dict.get(left_val, 0) > 0 and right_dict.get(right_val, 0) > 0 and not i%const:
            result += left_dict.get(left_val, 0) * right_dict.get(right_val, 0)
        
        left_dict[i] = left_dict.get(i, 0) + 1

    return result

if __name__ == "__main__":

    # variables here
    arr = [1,5,5,25,125]
    const = 5

    # calling methods
    start = time.time()
    # call method here
    result = count_triplets(arr, const)
    end = time.time()

    print(f"result: {result}")
    print(f"Total time taken: {end-start}")
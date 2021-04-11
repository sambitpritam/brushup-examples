import time


def frequency_queries(queries):
    result = list()

    summary_dict = dict()
    tmp_dict = dict()

    for i in queries:
        key = i[0]
        val = i[1]
        if key == 1:
            # increase frequecy of the number
            freq = summary_dict.get(val, 0) + 1
            summary_dict[val] = freq
            tmp_dict[freq]
        elif key == 2 and summary_dict.get(val, 0) > 0:
            # decrease frequncy of the number
            summary_dict[val] = summary_dict.get(val, 0) - 1
        elif key == 3:
            # insert 0/1 if there is any number with the value as frequency
            if val in summary_dict.values():
                result.append(1)
            else:
                result.append(0)
    return result

if __name__ == "__main__":
    # variables here
    queries = [[3,4], [2,1003], [1,16], [3,1]]
    start = time.time()
    # function call here
    result = frequency_queries(queries)
    end = time.time()
    print(f"result: {result}")
    print(f"Total time taken: {end-start}")
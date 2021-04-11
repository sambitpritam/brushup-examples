def get_largest():
    n = 10
    queries = [[1,5,100], [2,5,100], [3,4,100], [1,9,100], [2,3,100]]

    # result_arr = [0 for i in range(n)]
    # max_val = 0
    # index_count = {}

    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
        print(arr)
    maxval = 0
    itt = 0
    print(f"After For Loop: \n{arr}")
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    print(f"Max Value is: {maxval} ")
    return maxval

    # for elem in m:
    #     start = elem[0] - 1
    #     end = elem[1]

    #     for i in range(start, end):
    #         if i in index_count.keys():
    #             index_count[i] += 1
    #             if max_val < index_count[i] * elem[2]:
    #                 max_val = index_count[i] * elem[2]
    #         else:
    #             index_count[i] = 1

        # if start < m[run-1][0] and run > 0:
        #     start = m[run-1][0]

        # if end > m[run-1][1] and run > 0:
        #     end = m[run-1][1]

        # for idx in range(start, end):
        #     result_arr[idx] += elem[2]
        #     if max_val < result_arr[idx]:
        #         max_val = result_arr[idx]
        # print(result_arr)
        # run += 1

    
    



if __name__ == "__main__":
    # size of list
    n_lst = 5

    # no of operations
    m_lst = [[1,2,100], [2,5,100], [3,4,100]]

    get_largest()

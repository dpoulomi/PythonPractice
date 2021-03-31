def checkIfSumPresent(sum, arr, length):
    store = [[True for i in range(length + 1)]
                    for j in range(sum + 1)]

    for i in range(0, length + 1):
        store[0][i] = True
    for i in range(1, sum + 1):
        store[i][0] = False
    for i in range(1, sum + 1):
        for j in range(1, length + 1):
            if(store[i][0] > store[0][j]):
                store[i][j] = store[i - 1][j]
            else:
                store[i][j] = store[i - 1][j - store[i][0]]


    return store[sum][length]


def findIfEqualPartitionPresent(arr, length):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

    if(sum % 2 != 0):
        return False
    else:
        return checkIfSumPresent(sum // 2 , arr, length)



if __name__ == '__main__':
    # arr = [1, 5, 5, 11]
    arr = [3, 1, 1, 2, 2, 1]
    print(findIfEqualPartitionPresent(arr , len(arr)))

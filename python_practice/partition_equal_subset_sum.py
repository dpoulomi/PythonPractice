
# this code will work if there is only 1 element grouped with other elements in the array
def findIfPartitionPresentWith1Element(arr):
    sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if(i != j ):
                sum = sum + arr[j]
                if(sum > arr[i]):
                    break

        if(sum == arr[i]):
            print("Present")


4 , 5 , 8 , 1
def findIfPartitionPresent(arr , n):
    comparedSum = 0
    storedArray = [0] * n
    for i in range(len(arr)):
        comparedSum = comparedSum + arr[i]
        storedArray =
        for j in range(len(arr)):





if __name__ == '__main__':
    arr = [1, 5, 9, 5]
    # arr = [1, 3, 5]
    findIfPartitionPresent(arr , len(arr))
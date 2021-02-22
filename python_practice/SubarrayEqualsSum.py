

def getIndices(arr, sum, n):
    start = 0;
    # arr = [6, 8 , 9 , 0, 1]
    presentSum = arr[0]
    iter = start + 1
    #i = start + 1;
    for i in range(iter, n , 1):
        presentSum = presentSum + arr[i]
        if(presentSum == sum):
            print ("The start index " + start + "the end index is " + i)
            break;
        elif(presentSum > sum):
            start = start + 1
            presentSum = arr[start]
            iter = start + 1
            i = iter



arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23
n = 8

getIndices(arr, sum, n)
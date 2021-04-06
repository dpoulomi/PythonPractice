

def findKnapSackDynammicProgramming(value, weight, totalWeight):
    # storage = [0] * [len(value) + 1][totalWeight + 1]
    storage = [[0  for x in range(len(weight) + 1)]for x in range(totalWeight + 1)]
    for i in range(len(value) + 1):
        storage[i][0] = 0
    for i in range(totalWeight + 1):
        storage[0][i] = i

    for i in range(1 , len(value)):
        for j in range(1, totalWeight + 1):
            if(j - weight[i] > 0):
                storage[i][j] = max(weight[i] + storage[i - 1][j - weight[i]], storage[i - 1][j])
            else:
                storage[i][j] = storage[i - 1][j]

    return storage[value][totalWeight]
info@1stchoiceacupuncture.com






if __name__ == '__main__':
    value = [1, 4, 5 , 7]
    weight = [1, 3, 4, 5]
    totalWeight = 7
    print(findKnapSackDynammicProgramming(value, weight, totalWeight))


def findKnapSackDynammicProgramming(value, weight, totalWeight):
    # storage = [0] * [len(value) + 1][totalWeight + 1]
    storage = [[0  for x in range(totalWeight + 1)]for x in range(len(value) + 1)]

    for i in range(len(value) + 1):
        for j in range(totalWeight + 1):
            if(i == 0 or j == 0):
                storage[i][j] = 0
            if(j - weight[i - 1] >= 0):
                storage[i][j] = max(value[i - 1] + storage[i - 1][j - weight[i - 1]], storage[i - 1][j])
            else:
                storage[i][j] = storage[i - 1][j]

    return storage[len(value)][totalWeight]



if __name__ == '__main__':
    value = [1, 4, 5 , 7]
    weight = [1, 3, 4, 5]
    totalWeight = 7
    print(findKnapSackDynammicProgramming(value, weight, totalWeight))
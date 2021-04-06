def findMaxValueSubsetOfValue(value, weight, W, valueLength, calculatedWeight):
    if(W <= 0):
        return 0
    calculatedWeight = calculatedWeight + weight[valueLength - 1]
    if(calculatedWeight < W):
        print("")
    elif(weight[valueLength - 1] > W):
        findMaxValueSubsetOfValue(value, weight, W, valueLength - 1)
    return findMaxValueSubsetOfValue(value, weight, W, valueLength - 1) or findMaxValueSubsetOfValue(value, weight, W - weight[valueLength - 1], valueLength - 1)

def knapSackValue(value, weight, W, valueLength, weightList, valueList):
    if valueLength == 0 or W == 0:
        return 0
    if(weight[valueLength - 1] > W):
        return knapSackValue(value, weight, W, valueLength - 1, weightList, valueList)
    else:
        return max(value[valueLength - 1] +
                      knapSackValue(value, weight, W- weight[valueLength -1], valueLength - 1, weightList, valueList),
                      knapSackValue(value, weight, W, valueLength - 1, weightList, valueList))


def findKnapSackValue(value, weight, W, calculatedWeight, valueLength, list, valueList):
    if(valueLength <= 0):
        return
    calculatedWeight = calculatedWeight + weight[valueLength - 1]
    if(calculatedWeight <= W):
        list.append([weight[valueLength - 1]])
        valueList.append([value[valueLength - 1]])
        # findKnapSackValue(value, weight, W, calculatedWeight, valueLength - 1, list, valueList)
    elif(calculatedWeight > W):
        calculatedWeight = calculatedWeight - weight[valueLength - 1]
        # list.remove([weight[valueLength - 1]])
    findKnapSackValue(value, weight, W, calculatedWeight, valueLength - 1, list, valueList ) or findKnapSackValue(value, weight, W - weight[valueLength - 1], calculatedWeight, valueLength - 1, list, valueList )


if __name__ == '__main__':
    W = 7
    # weight = [10, 20, 30]
    # value = [60, 100, 120]
    weight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    valueLength = len(value);
    wight_list = [];
    value_list = []
    calculatedWeight = 0;
    print(knapSackValue(value, weight, W, valueLength, wight_list, value_list))
    # findKnapSackValue(value , weight , W, calculatedWeight,valueLength ,wight_list, value_list)
    # print("Weights: ")
    # for i in wight_list:
    #     print(i)
    # print("Values: ")
    # for j in value_list:
    #     print(j)
    # findMaxValueSubsetOfValue(value, weight, W, valueLength, calculatedWeight)

def removeDuplicates(givenString):
    hash = [0] * 256
    fastIndicator = 0
    finalIndicator = 0
    temp = ''
    processedString = convertToMutableString(givenString)
    while(fastIndicator != len(processedString)):
        temp = processedString[fastIndicator]
        if (hash[ord(temp)] == 0):
            hash[ord(temp)] = 1
            processedString[finalIndicator] = processedString[fastIndicator]
            finalIndicator = finalIndicator + 1;
        fastIndicator = fastIndicator + 1

    return processedString[0: finalIndicator]


def convertToMutableString(givenString):
    List = []
    for i in givenString:
        List.append(i)
    return List




if __name__ == '__main__':
    givenString = "geeksforgeeks"
    print(removeDuplicates(givenString))
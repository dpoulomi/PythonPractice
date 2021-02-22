def reverseSentence():
    sentence = "I love to code and always try new things."
    print(sentence)
    newString = ""
    reversedString = ""
    words = sentence.split(' ')
    for i in words:
       newString = newString + " " + reverseWords(i)
    #print (newString)
    reversedString =  reverseWords(newString)
    print (reversedString)



def reverseWords(word):
    start = 0 ;
    end = len(word) -  1;
    newString = ''
    while(start <= end):
        lst = list(word)
        lst[start], lst[end] = lst[end], lst[start]
        newString = "".join(lst)
        word = newString
        start = start + 1
        end = end - 1

    return newString

if __name__ == '__main__':
    reverseSentence()
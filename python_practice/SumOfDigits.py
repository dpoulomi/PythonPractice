

def findSum(num):
 sum = 0
 while(num != 0):
     sum = sum +  num % 10
     num = num // 10

 return sum

num = 890
print (findSum(num))


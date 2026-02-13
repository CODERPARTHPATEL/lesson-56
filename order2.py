# program tofins the element not making a pair

#function to calcuate the number that is odd occurring

def oddoccurring(arr):
    # initialize result
    res = 0

    # traverse the array
    for element in arr:
        #xor with the result
        res = res ^ element

    return res

#initialize our array
arr = []

#take array size as input
n = int(input('enter array size:'))



while(n):
    num = int(input('enter number:'))
    arr.append(num)
    n-=1

print('\n\nodd occurring number is:',oddoccurring(arr))
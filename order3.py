# program to find two numbdrs that are odd
def printtwoodd(arr, size):
    
    #variable tohold 2 odd numbers
    xorof2 = arr[0]

    #holds two odd numbers
    x = 0
    y = 0


# this will hold right most xorof2

    setbit = 0
    
    for i in range(1,size):
        xorof2 = xorof2 ^ arr[1]

    setbit = xorof2 & ~(xorof2 - 1)
    for i in range(size):
        if(arr[i]& setbit):
            x = x ^arr[i]
        else:
            y = y ^ arr[i]
    print('the two odd element are', x, '&', y)
# creat empty array
arr = []

arr_size = int(input('enter size of aray:'))
for i in range(0,arr_size):
    z = int(input('enter element:'))
    arr.append(z)
printtwoodd(arr,arr_size)

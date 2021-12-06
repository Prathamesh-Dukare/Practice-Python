import os
def longestSubarray(arr):
    for j in range(1,len(arr)+1):
        for i in range(0,len(arr)):
            print(arr[i])
                
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
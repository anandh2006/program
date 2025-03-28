def first_index(arr, x, index=0):
 
    if index == len(arr):
        return -1
    
    if arr[index] == x:
        return index  

    return first_index(arr, x, index + 1)

arr = [4, 1, 2, 5, 2]
x = 2
print(first_index(arr, x))  

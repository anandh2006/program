def is_sorted(arr, index=0):
    
    if index == len(arr) - 1:
        return True  

    if arr[index] > arr[index + 1]:
        return False  

    return is_sorted(arr, index + 1)

arr1 = [1, 2, 3, 4, 5]

print(is_sorted(arr1))  


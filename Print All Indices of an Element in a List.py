def all_indices(arr, x, index=0, indices=[]):

    if index == len(arr):
        return indices

    if arr[index] == x:
        indices.append(index)

    return all_indices(arr, x, index + 1, indices)

arr = [4, 2, 1, 2, 5, 2]
x = 2
print(all_indices(arr, x))  

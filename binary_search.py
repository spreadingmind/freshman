#Given a sorted array arr[] of n elements,
# write a function to search a given element x in arr[].

arr = [1, 2, 4, 5, 5, 6, 6, 6, 25]

def binary_search(arr, val):
    if arr:
        middle = len(arr) // 2
        if val == arr[middle]:
            return True
        else:
            if val < arr[middle]:

                return binary_search(arr[:middle], val)
            else:
                return binary_search(arr[middle+1:], val)

    else:
        return False


print (binary_search(arr, 6))
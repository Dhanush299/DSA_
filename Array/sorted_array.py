def sorted_array(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    
    
    
arr=[1,3,4,5,2,6,7,10]
print(sorted_array(arr))
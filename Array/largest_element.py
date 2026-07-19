def largest_ele(arr):
    lar=0
    for ele in arr:
        if ele>lar:
            lar=ele
    return lar
arr=[5,4,1,10,4,2]
print(largest_ele(arr))
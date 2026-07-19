def second_lar(arr):
    first_lar=0
    second_lar=0
    for num in arr:
        if num > first_lar:
           
            second_lar=first_lar
            first_lar=num
        if num > second_lar and num<first_lar:
            second_lar=num
    return second_lar
    
    
    
    
    
arr=[4,3,5,6,7,10,10,9,11]
print(second_lar(arr))
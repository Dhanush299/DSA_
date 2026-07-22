# def left_rotate(arr,k):
#     n=len(arr)
#     k=k%n
#     temp=[]
#     for i in range(k,n):
#         temp.append(arr[i])
        
#     for i in range(k):
#         temp.append(arr[i])
#     return temp

# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 2

# print(left_rotate(arr, k))

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def left_rotate(arr,k):
    n=len(arr)
    k=k%n
    
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k=2
print(left_rotate(arr,k))
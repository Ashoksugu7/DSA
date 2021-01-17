#insertion sort in the array

def insertion(arr):

    for i in range(1, len(arr)):
        j=i-1
        x=arr[i]

        while j >= 0 and arr[j] > x:
            arr[j+1]=arr[j]
            j-=1
            #print(arr, x)

        arr[j+1]=x



    return arr


arr = [2,5,7,8,1,2,9]

print(insertion(arr))
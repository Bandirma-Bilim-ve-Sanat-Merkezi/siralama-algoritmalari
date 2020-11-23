def parcala(arr, kucuk, buyuk): 
    i = ( kucuk-1 )
    #en kucuk elemanı pivot olarak aldık
    pivot = arr[kucuk] 
    
    #pivota göre parçalama
    for _ in range(kucuk , buyuk): 
  
        if   arr[_] < pivot: 
          
            i = i+1 
            arr[i],arr[_] = arr[_],arr[i] 
  
    arr[i+1],arr[buyuk] = arr[buyuk],arr[i+1] 

    return ( i+1 ) 

#sıralama
def quick(arr, kucuk, buyuk): 
    if kucuk< buyuk: 

        pi = parcala(arr, kucuk, buyuk) 
        quick(arr, kucuk, pi-1) 
        quick(arr, pi+1, buyuk)

    return arr
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
arr = quick(arr, 0, n-1)
print(arr)

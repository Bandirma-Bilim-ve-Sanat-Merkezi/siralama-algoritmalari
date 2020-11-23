def insert(listt): 
    
    #birden başlayarak listenin uzunluğuna kadar gidecek bir döngü
    for _ in range(1, len(listt)): 
        
        #bulunduğumuz geçiş
        sira = arr[_] 
  
        esk = _-1
        while sira < listt[esk] and esk >= 0: 
                listt[esk + 1] = listt[esk] 
                esk -= 1
        listt[esk + 1] = sira
        
    return listt

listt = [12, 11, 13, 5, 6] 
arr = insert(listt)
print(arr)

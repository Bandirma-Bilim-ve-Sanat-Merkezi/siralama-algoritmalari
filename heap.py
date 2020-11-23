def agac_olustur(listt, lenn, maxel):
    root = maxel

    #root elemanın solundaki değer
    l = 2 * maxel + 1

    #root elemanın sağındaki değer
    r = 2 * maxel + 2

    #root eleman ile karşılaştırma
    if l < lenn and listt[root] < listt[l]:
        root = l

    #root eleman ile karşılaştırma
    if r < lenn and listt[root] < listt[r]:
        root = r

    #eğer ağac yanlışsa tekrar düzenlenir
    if root != maxel:
        listt[maxel], listt[root] = listt[root], listt[maxel]

        agac_olustur(listt, lenn, root)

#şimdi ise sıralama
def heapSort(listt):
    lenn = len(listt)
 
    for i in range(lenn//2-1, -1, -1):
        agac_olustur(listt, lenn, i)
 
    for i in range(lenn-1, 0, -1):
        listt[i], listt[0] = listt[0], arr[i]
        agac_olustur(listt, i, 0)
    
    return arr

arr = [9, 25, 8, 2, 15, 13]
arr = heapSort(arr)

print(arr)

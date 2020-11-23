#fonskiyon oluşturup listemi aldım
def BubbleSort(liste):

    #listemin uzunluğunu aldım -> len()
    lenn = len(liste)

    #geçişleri belirleyecek döngüm
    for _ in range(lenn):

        #tüm yan yana olan ikilileri gezmeme yarayacak döngüm. lenn-_-1 yaparak sıralanmış elemanlara tekrar gitmemeyi sağladım. Böylece işlem hızlanacak
        for __ in range(0, lenn-_-1):

            #sıralamada bir yanlışlık var ise...
            if liste[__]>liste[__+1]:

                #...elemanların yerlerini değiştir.
                liste[__], liste[__+1] = liste[__+1], liste[__]
            print(list)

    #listeyi döndür
    return list

#listemi verdim
listem = [1,5,9,2,7]

print(listem)

#fonksiyonu çağırıp listem değişkenine eşitledim
listem = BubbleSort(listem)
print(listem)

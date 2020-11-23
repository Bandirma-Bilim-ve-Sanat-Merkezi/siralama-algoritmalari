def mergeSort(listt):

    #array bir elemandan büyükse diye bir kontrol yapıyoruz. Eğer küçükse veya eşitse bölemeyiz
    if len(listt) > 1:
 
        #Ortakadi elemanı buluyoruz
        mid = len(listt)//2
 
        #Ortadaki elemandan ikiye bölüyoruz
        solparca = listt[:mid]
 
        #sağdaki parcamız
        sagparca = listt[mid:]
 
        #İki parçayı da parçalamaya devam ediyoruz
        mergeSort(solparca)
 
        #Diğer parçayı parçalıyoruz
        mergeSort(sagparca)
 
        mi = 0
        mkek = 0
        mss = 0
 
        # temp diziler oluşturuyoruz
        while mi < len(solparca) and mkek < len(sagparca):
            if solparca[mi] < sagparca[mkek]:
                listt[mss] = solparca[mi]
                mi += 1
            else:
                listt[mss] = sagparca[mkek]
                mkek += 1
            mss += 1

        #Diğer parçayı da
        while mkek < len(sagparca):
            listt[mss] = sagparca[mkek]
            mkek += 1
            mss += 1

        # Parcaları kontrol ediyoruz
        while mi < len(solparca):
            listt[mss] = solparca[mi]
            mi += 1
            mss += 1

    return listt

listt = [5, 6, 9, 8, 2, 4, 787, 9]
print(listt)
listt = mergeSort(listt)

print(listt)

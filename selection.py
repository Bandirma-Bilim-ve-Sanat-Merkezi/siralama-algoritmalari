#fonskiyon oluşturup sıralanacak listemizi parametre olarak alıyoruz
def selection(liste):
    
    #listenin uzunluğu kadar dönecek bir for döngüsü oluşturuyoruz
    for i in range(len(liste)):

        #minimum elemanımızı belirliyoruz
        enkucuk = i

        #sıralanmamış alt dizimizin içinde dönüyoruz. i+1 bu işe yarıyor.
        for _ in range(i+1, len(liste)):

            #en küçük elemanımızı bulup başa yerleştireceğiz
            if liste[enkucuk] > liste[_]:
                enkucuk = _

        #yer değiştirme işlemi
        liste[i], liste[enkucuk] = liste[enkucuk], liste[i]

    #girilen listemizi döndürüyoruz
    return liste

#listemi oluşturdum
lism = [65, 51, 23, 48]
print(lism)

#fonskiyonu çağırıp döndürdüğü veriyi lism değişkenine atadım
lism = selection(lism)
print(lism)

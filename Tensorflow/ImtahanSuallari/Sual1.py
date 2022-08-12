# Sual1 -- 10 balliq
liste = [1, 2, 3, 4, 5, 6]


# 1.1 listin icindeki deyerleri toplaya bilen funksiya yazin
# 1.2 listin icindeki funksiyalari bir birile vurub hasil cixarda bilen
# 1.3 input verildikde listin icine elave ede bilecek,inputda 'remove' yazdiqda ilk indexdexdeki deyeri remove ede bilecek funksiya yazin
# 1.4 ele funksiya  yazin ki listin icerisindeki cut edelerin ceminden tek ededlerin cemin cixsin
# 1.5 ele funksiya yazin ki listin icerisindeki cut ededlerin hasilini tek ededlerin hasiline bolsun

def hasil(liste):
    """ 1.2 listin icindeki funksiyalari bir birile vurub hasil cixarda bilen """
    x = 1
    for i in liste:
        x *= i
    return x


def topla(siyahi):
    """ 1.1 listin icindeki deyerleri toplaya bilen funksiya yazin """
    x = 0
    for i in siyahi:
        x += i
    return x


print(topla(liste))

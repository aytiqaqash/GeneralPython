# Sual1 -- 10 balliq
liste = [1, 2, 3, 4, 5, 6]


# 1.1 listin icindeki deyerleri toplaya bilen funksiya yazin
# 1.2 listin icindeki funksiyalari bir birile vurub hasil cixarda bilen
# 1.3 input verildikde listin icine elave ede bilecek,inputda 'remove' yazdiqda ilk indexdexdeki deyeri remove ede bilecek funksiya yazin
# 1.4 ele funksiya  yazin ki listin icerisindeki cut edelerin ceminden tek ededlerin cemin cixsin
# 1.5 ele funksiya yazin ki listin icerisindeki cut ededlerin hasilini tek ededlerin hasiline bolsun

def cut_bol_tek(liste):
    """ 1.5 ele funksiya  yazin ki listin icerisindeki cut ededlerin hasilini tek ededlerin hasiline bolsun """
    cutHasil, tekHasil = 1, 1
    for i in liste:
        if i % 2 == 0:
            cutHasil *= i
        else:
            tekHasil *= i

    if tekHasil == 0:
        return 0
    return cutHasil / tekHasil


def cut_cix_tek(liste):
    """ 1.4 ele funksiya  yazin ki listin icerisindeki cut edelerin ceminden tek ededlerin cemin cixsin """
    cutSum, tekSum = 0, 0
    for i in liste:
        if i % 2 == 0:
            cutSum += i
        else:
            tekSum += i
    return cutSum - tekSum


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

# Sual2 -- 10 balliq
liste = [2, 3, 4, 5, 6]
liste2 = [9, 8, 8, 9, 3]


# 2.1 iki listi birleshdirb icerisindeki unique olanlari cixartsin
# 2.2 iki listin her birinin kvadrat listin  cixartsin sonra ise iki kvadratlar listindeki deyerleri  bir birile muqayise etsin
# 2.3 ele funksiya yazIn ki hem her listin cemin , hasilin tapsin sonra ise birinci listin cemi ile ikincin listin cemin , birinci listin hasili ile ikinci listi hasilin muqayise etsin
# 2.4 her listdeki unique deyerleri tapsin yigsin bir liste sonra ise ollarin hasilin tapsin
# 2.5 deyerleri stringe cevirsin sonra ise onlari bosh bir stringde birleshdirsin

def unique_values(liste, liste2):
    """ iki listi birleshdirb icerisindeki unique olanlari cixartsin """
    return set(liste + liste2)


def sqrt_of_list_items(liste):
    return [i ** 2 for i in liste]


def compare_lists(liste, liste2):
    return set([str(i) + " == " + str(x) + " => " + str(i == x) for i in liste for x in liste2])


def task2_3(list1, list2):
    """ 2.3 ele funksiya yazIn ki hem her listin cemin ,
    hasilin tapsin sonra ise birinci listin cemi ile ikincin listin cemin ,
    birinci listin hasili ile ikinci listi hasilin muqayise etsin """
    cem1 = topla(list1)
    cem2 = topla(list2)
    hasil1 = hasil(list1)
    hasil2 = hasil(list2)
    if cem1 > cem2:
        muqayiseCem = "çoxdur"
    elif cem1 < cem2:
        muqayiseCem = "azdır"
    else:
        muqayiseCem = "bərabərdir"

    if hasil1 > hasil2:
        muqayiseHasil = "çoxdur"
    elif hasil1 < hasil2:
        muqayiseHasil = "azdır"
    else:
        muqayiseHasil = "bərabərdir"

    print("Birinci listin cəmi, ikinci listin cəmindən: " + muqayiseCem + "!")
    print("Birinci listin hasili, ikinci listin hasilindən: " + muqayiseHasil + "!")


def topla(siyahi):
    """ 1.1 listin icindeki deyerleri toplaya bilen funksiya yazin """
    x = 0
    for i in siyahi:
        x += i
    return x


def hasil(liste):
    """ 1.2 listin icindeki funksiyalari bir birile vurub hasil cixarda bilen """
    x = 1
    for i in liste:
        x *= i
    return x


def task2_4(list1, list2):
    """ her listdeki unique deyerleri tapsin yigsin bir liste sonra ise ollarin hasilin tapsin """
    unikal1 = set(list1)
    unikal2 = set(list2)
    res = list(unikal1) + list(unikal2)
    return hasil(res)


# @TODO Understand task 2.5 and release.
def task2_5():
    pass

print(unique_values(liste, liste2))
print(compare_lists(sqrt_of_list_items(sorted(liste)), sqrt_of_list_items(sorted(liste2))))
task2_3(liste, liste2)
print(task2_4(liste, liste2))




# Sual 3 -- 15 balliq
# Sual bir ve ikini class seklinde yazin, ikinci classi birinci classdan inherit eliyin

class ImtahanSual1:
    """ Birinci sualın funksiyaları burada """

    def __init__(self, liste=None, liste2=None):
        if liste2 is None:
            liste2 = []
        if liste is None:
            liste = []
        self.liste = liste
        self.liste2 = liste2

    def listiDeyish(self, liste=[]):
        """ 1.3 input verildikde listin icine elave ede bilecek,inputda 'remove' yazdiqda ilk indexdexdeki deyeri remove ede bilecek funksiya yazin """
        if liste == []:
            liste = self.liste
        x = str(input())
        if x == "remove":
            liste.pop(0)
        else:
            liste.append(x)
        return liste

    def cut_bol_tek(self, liste=[]):
        """ 1.5 ele funksiya  yazin ki listin icerisindeki cut ededlerin hasilini tek ededlerin hasiline bolsun """
        if liste == []:
            liste = self.liste
        cutHasil, tekHasil = 1, 1
        for i in liste:
            if i % 2 == 0:
                cutHasil *= i
            else:
                tekHasil *= i

        if tekHasil == 0:
            return 0
        return cutHasil / tekHasil

    def cut_cix_tek(self, liste=[]):
        """ 1.4 ele funksiya  yazin ki listin icerisindeki cut edelerin ceminden tek ededlerin cemin cixsin """
        if liste == []:
            liste = self.liste
        cutSum, tekSum = 0, 0
        for i in liste:
            if i % 2 == 0:
                cutSum += i
            else:
                tekSum += i
        return cutSum - tekSum

    def hasil(self, liste=[]):
        """ 1.2 listin icindeki funksiyalari bir birile vurub hasil cixarda bilen """
        if liste == []:
            liste = self.liste
        x = 1
        for i in liste:
            x *= i
        return x

    def topla(self, liste=[]):
        """ 1.1 listin icindeki deyerleri toplaya bilen funksiya yazin """
        if liste == []:
            liste = self.liste
        x = 0
        for i in liste:
            x += i
        return x


class ImtahanSual2(ImtahanSual1):
    def __init__(self, l1=[], l2=[]):
        super().__init__()
        self.l1 = l1
        self.l2 = l2

    def unique_values(self, l1=[], l2=[]):
        """ iki listi birleshdirb icerisindeki unique olanlari cixartsin """
        if l1 == []:
            l1 = self.l1
        if l2 == []:
            l2 = self.l2
        return set(l1 + l2)

    def sqrt_of_list_items(self,liste=[]):
        if liste==[]:
            liste = self.liste
        return [i ** 2 for i in liste]

    def compare_lists(self,l1=[],l2=[]):
        if l1==[]:
            l1=self.l1
        if l2==[]:
            l2=self.l2
        return set([str(i) + " == " + str(x) + " => " + str(i == x) for i in l1 for x in l2])

    def task2_3(self, l1=[],l2=[]):
        """ 2.3 ele funksiya yazIn ki hem her listin cemin ,
        hasilin tapsin sonra ise birinci listin cemi ile ikincin listin cemin ,
        birinci listin hasili ile ikinci listi hasilin muqayise etsin """

        if l1==[]:
            l1=self.l1
        if l2==[]:
            l2=self.l2

        cem1 = self.topla(l1)
        cem2 = self.topla(l2)
        hasil1 = self.hasil(l1)
        hasil2 = self.hasil(l2)
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

    def task2_4(self, list1=[], list2=[]):
        """ her listdeki unique deyerleri tapsin yigsin bir liste sonra ise ollarin hasilin tapsin """
        if list1 == []:
            list1 = self.l1
        if list2 == []:
            list2 = self.l2

        unikal1 = set(list1)
        unikal2 = set(list2)
        res = list(unikal1) + list(unikal2)
        print(res)
        return self.hasil(res)

    # def main(self):
    #
    # if __name__ == "__main__":
    #     main()


liste = [1, 2, 3, 4, 5, 6]
liste2 = [9, 8, 8, 9, 3]

print("------ Imatahan suallari 1 -----------")

x = ImtahanSual1(liste)
print("Summary: " + str(x.topla()))
print("Multiplication: " + str(x.hasil()))
print("Difference of multiplication even and odd of the list: " + str(x.cut_cix_tek()))
print("Divide of multiplication even and odd of the list: " + str(x.cut_bol_tek()))


print("------ Imatahan suallari 2 -----------")

y = ImtahanSual2(liste, liste2)

print(y.unique_values())
print(y.compare_lists(y.sqrt_of_list_items(sorted(liste)), y.sqrt_of_list_items(sorted(liste2))))
y.task2_3(liste, liste2)
print(y.task2_4(liste, liste2))

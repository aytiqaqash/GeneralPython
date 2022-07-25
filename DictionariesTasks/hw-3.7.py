# 7. for dongusu vasitesile dictionary-nin icinde olan hermliste deyer assign edin uygun sekilde
# ve esas key-in deyeri olan dictionarynin icersine key_value pairi elave edin
liste = [{'name':{'oglan_adlari':['Nizami','Elsen','Ulvi'],'qiz_adlari':['Aygun','Sehla','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','Haciyev'],'qizlarin_soyadlari':['Rehmanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','orta','ali'],'qizlarin_tehsili':['ali','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,34],'qizlarin_yasi':[24,26,27]}},{'name':{'oglan_adlari':['Etibar','Elsen','REsad'],'qiz_adlari':['Aygun','Aygul','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','VEliyev'],'qizlarin_soyadlari':['Sabanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','ali','ali'],'qizlarin_tehsili':['orta','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,45],'qizlarin_yasi':[21,26,27]}}]
#Numune 1.['Nizami','Elsen','Ulvi','Resad']
#Numune 2. {'oglanlarin_yasi':[29,32,45],'qizlarin_yasi':[21,26,27]} ==> {'oglanlarin_yasi':[29,32,45],'qizlarin_yasi':[21,26,27],'all_age':[29,32,45,21,26,27]}
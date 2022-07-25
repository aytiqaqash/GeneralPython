# 5.  for dongusu yazin ki listin icindeki iki dictionarynin value-larin muqayise etsin
liste = [{'name':{'oglan_adlari':['Nizami','Elsen','Ulvi'],'qiz_adlari':['Aygun','Sehla','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','Haciyev'],'qizlarin_soyadlari':['Rehmanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','orta','ali'],'qizlarin_tehsili':['ali','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,34],'qizlarin_yasi':[24,26,27]}},
         {'name':{'oglan_adlari':['Etibar','Elsen','REsad'],'qiz_adlari':['Aygun','Aygul','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','VEliyev'],'qizlarin_soyadlari':['Sabanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','ali','ali'],'qizlarin_tehsili':['orta','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,45],'qizlarin_yasi':[21,26,27]}}]
# HINT: in,not in

for lughet in liste[0]:
  if lughet in liste[1]:
    for item in liste[0][lughet]:
      if item in liste[1][lughet]:
        for val in liste[0][lughet][item]:
          if val in liste[1][lughet][item]:
            print(str(val) + " is in both dictionaries!")
          else:
            print(str(val) + " is only in the first dictionary!")
  else:
    for lughet2 in liste[1]:
      if lughet2 not in liste[0]:
        for item in liste[1][lughet2]:
          if item in liste[0][lughet]:
            for val in liste[1][lughet2][item]:
              if val in liste[0][lughet][item]:
                print(str(val) + " is in both dictionaries!")
              else:
                print(str(val) + " is only in the second dictionary!")
# 3. for dongusu yazin listlerin icersinde sadece bir deyer saxlasin digerlerin drop etsin yeni silsin
dictionary = {'name':{'oglan_adlari':['Nizami','Elsen','Ulvi'],'qiz_adlari':['Aygun','Sehla','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','Haciyev'],'qizlarin_soyadlari':['Rehmanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','orta','ali'],'qizlarin_tehsili':['ali','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,34],'qizlarin_yasi':[24,26,27]}}

for k, v in dictionary.items():
  if type(v) == list and len(v)>1:
    for i in v:
          v.remove(i)
  else:
    for nv in v.values():
      if type(nv) == list and len(nv)>1:
        for i in nv:
          nv.remove(i)

print(dictionary)

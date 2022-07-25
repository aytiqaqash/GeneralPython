# 2. for dongusu yazin ki dictionarydeki butun listleri bosh bir liste daxil etsin
dictionary = {'name':{'oglan_adlari':['Nizami','Elsen','Ulvi'],'qiz_adlari':['Aygun','Sehla','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','Haciyev'],'qizlarin_soyadlari':['Rehmanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','orta','ali'],'qizlarin_tehsili':['ali','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,34],'qizlarin_yasi':[24,26,27]}}
# Numune ==> a = ['Nizami',Elsen',Ulvi','Aygun','Sehla','Ulker','Aliyev','Quliyev','Haciyev','Rehmanova','Quliyeva','Ismayilova','ali','orta','ali']

all_lists = []
for k, v in dictionary.items():
  if type(v) == list:
    for i in v:
          all_lists.append(i)
  else:
    for nv in v.values():
      if type(nv) == list:
        for i in nv:
          all_lists.append(i)
# 1. for dongusu yazin ki butun matchin olan olan melumatlari cixartsin
dictionary = {'name':{'oglan_adlari':['Nizami','Elsen','Ulvi'],'qiz_adlari':['Aygun','Sehla','Ulker']},
          'soyad':{'oglanlarin_soyadlari':['Aliyev','Quliyev','Haciyev'],'qizlarin_soyadlari':['Rehmanova','Quliyeva','Ismayilova']},
          'tehsil':{'oglanlarin_tehsili':['ali','orta','ali'],'qizlarin_tehsili':['ali','ali','ali']},
          'yas':{'oglanlarin_yasi':[29,32,34],'qizlarin_yasi':[24,26,27]}}
# Numune ==> Nizami Aliyev ali 29, Elsen Quliyev orta 32, Ulvi Haciyev ali 34
# bunu hamsi ucun edin

Name = []
LName = []
Education = []
Age = []
for key,vals in dictionary.items():
  if key == 'name':
    for x in vals.values():
      for i in x:
        Name.append(i)
  elif key == 'soyad':
    for x in vals.values():
      for i in x:
        LName.append(i)
  elif key == 'tehsil':
    for x in vals.values():
      for i in x:
        Education.append(i)
  elif key == 'yas':
    for x in vals.values():
      for i in x:
        Age.append(i)

result = ''
for i in range(len(Name)):
  result = result + Name[i] + " " + LName[i] + " " + Education[i] + " " + str(Age[i])
  if i < len(Name)-1:
    result += ", "

print(result)
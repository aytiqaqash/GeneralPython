list = [1, 2, 1, 3, 2]
newList = []
for i in list:
  if i in newList:
    print(str(i) + " - dubl")
  else:
    newList.append(i)
    print(str(i) + " -  не встречалось ")

# Input:  [1, 2, 1, 3, 2]
# Output:
# 1 - not mentioned
# 2 - not mentioned
# 1 - duplicate
# 3 - not mentioned
# 2 - duplicate


list = [1, 2, 1, 3, 2]
newList = []
for i in list:
  if i in newList:
    print(str(i) + " - duplicate")
  else:
    newList.append(i)
    print(str(i) + " - not mentioned")

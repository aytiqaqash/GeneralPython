input_data = [58, 111, 93, 72, 100]

n = len(input_data) # uzunluğunu götürür

for i in range(1, n): # i - her element
  print(" n(" + str(n) + ") - i(" + str(i) + ") | Будем проверять: " + str(n - i) + " не сортированных элемента!")
  for j in range(n-i):
    # n-i sağa yığılan rəqəmləri  yoxlamasın deyədir
    print("Сравниваем " + str(input_data[j]) + " с " + str(input_data[j+1]))
    if input_data[j+1] < input_data[j]:
      print(" Меняем местами, т.к. " + str(input_data[j]) + " больше, чем " + str(input_data[j+1]) )
      tmp = input_data[j]
      input_data[j] = input_data[j+1]
      input_data[j+1] = tmp
    else:
      print("Не надо менять местами, т.к. " + str(input_data[j]) + " меньше " + str(input_data[j+1]))

print(input_data)
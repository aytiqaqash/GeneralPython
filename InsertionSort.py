def insertion_sort(list):
    for i in range(1, len(list)):  # 1, 8
        print("addım: " + str(i))
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            print("əvvəlki element " + str(j) + " sıfırdan çoxdur bərabərdir və " + str(
                key) + " götürdüyümüz element " + str(
                list[j]) + "dən azdır?")
            print("bəli, yerdəyişmə edirik: " + str(list[j + 1]) + " və " + str(list[j]))
            print(list)
            list[j + 1] = list[j]
            j -= 1
            list[j + 1] = key
            print(list)
    print()
    print("SON NƏTİCƏ: ")
    return list


not_sorted_list = [12, 5, 3, 1, 8, 7, 2, 4]  # [12]
print(insertion_sort(not_sorted_list))

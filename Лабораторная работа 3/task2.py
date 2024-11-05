# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, razdelitel = ","):
    list1 = str1.split(razdelitel)
    list2 = str2.split(razdelitel)
    list_common = []
    for i in list1:
        for j in list2:
            if i == j:
                list_common.append(i)
    list_common.sort()
    return list_common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
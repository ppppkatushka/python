def find_common_participants (s1, s2, raz = ","):
    fam1 = []
    fam2 = []
    fam1 = s1.split(raz)
    fam2 = s2.split(raz)
    itog =[]
    u=0
    for i in range (3):
        for j in range (3):
            if (fam1[i] == fam2[j]):
                itog.append(fam1[i])
    itog.sort()
    return itog


raz = "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, raz))
# TODO Провеьте работу функции с разделителем отличным от запятой

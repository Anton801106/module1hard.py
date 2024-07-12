students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

avarage_Aaron = sum(grades[0]) / len(grades[0])
print(avarage_Aaron)
avarage_Bilbo = sum(grades[1]) / len(grades[1])
print(avarage_Bilbo)
avarage_Johnny = sum(grades[2]) / len(grades[2])
print(avarage_Johnny)
avarage_Khendrik = sum(grades[3]) / len(grades[3])
print(avarage_Khendrik)
avarage_Steve = sum(grades[4]) / len(grades[4])
print(avarage_Steve)

avarage_grades = {'Aaron': avarage_Aaron, 'Bilbo': avarage_Bilbo, 'Johnny': avarage_Johnny, 'Khendrik': avarage_Khendrik, 'Steve': avarage_Steve}
print(avarage_grades)
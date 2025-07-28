def obtain_grade(mark):
    if 100 >= mark > 84.5:
        return 'A+'
    elif 84.5 >= mark > 79.5:
        return 'A'
    elif 79.5 >= mark > 74.5:
        return 'B+'
    elif 74.5 >= mark > 69.5:
        return 'B'
    elif 69.5 >= mark > 64.5:
        return 'C+'
    elif 64.5 >= mark > 59.5:
        return 'C'
    elif 59.5 >= mark > 54.5:
        return 'D+'
    elif 54.5 >= mark > 49.5:
        return 'D'
    elif mark <= 49.5:
        return 'F'


mark_list = [['Mary', 90.5], ['Charles', 60.4], [
    'John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]

print("Student Name   Marks     Grade  ")
for name, mark in mark_list:
    grade = obtain_grade(mark)
    print(f"{name:<15} {mark:<9} {grade:<7}")

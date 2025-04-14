from student import Student 
import trivia_questions
import sorting_ceremony
import wizarding_match

if __name__ == '__main__':
    num_users = int(input("How many fresh-faced young witches and wizards have joined our ranks this year? "))
    print("Let the Sorting Ceremony commence!")
    students = []
    for i in range (num_users):
        name, house= sorting_ceremony.sorting_ceremony()
        s = Student(name, house)
        students.append(s)
        if house != "muggle":
            print(name, "you belong in...", house+"!")
        if i < num_users - 1:
            print("Would the next young wizard please step forward!")
    print("\nNow that all are sorted, it's time for a test of wit! Answer wisely to earn points for the House Cup—may the best house triumph!\n")
   
    for student in students:
        student.points = trivia_questions.trivia(student.name)
        print(student.points)
    
    G_points = 0
    R_points = 0
    S_points = 0
    H_points = 0
    m_points = 0
    for student in students:
        if student.house == "Gryffindor":
             G_points += student.points
        elif student.house == "Slytherin":
             S_points += student.points
        elif student.house == "Ravenclaw":
             R_points += student.points
        elif student.house == "Hufflepuff":
             H_points += student.points
        else:
             m_points += student.points
house_points = {"Gryffindor": G_points, "Ravenclaw": R_points, "Slytherin": S_points, "Hufflepuff": H_points, "muggle": m_points}
cup_winner = max(house_points, key = house_points.get)

'''
total_points = []
for value in house_points.values():
     total_points.append(value)
org_list = total_points.sort()
if org_list[-1] == org_list[-2]:
'''


print("And the House Cup winner is!!! Count down with me!")
print('5...')
input()
print('4...')
input()
print('3...')
input()
print('2...')
input()
print('1!!!')
input()
print(cup_winner+'!!!!!!!')
    






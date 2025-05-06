from student import Student 
import trivia_questions
import sorting_ceremony
import wizarding_match

if __name__ == '__main__':

     while True:
          try:
               num_users = int(input("How many fresh-faced young witches and wizards have joined our ranks this year? "))
               break
          except:
               print("Ah, seems like you've cast a charm of confusion. Please enter a whole number, dear wizard.")

     if num_users == 0:
        print("Curiously, there are no new students this year. Still, perhaps next year will bring new minds through the castle gates.")
        exit()
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
     print("\nNow that all are sorted, it's time for a test of wit! Answer wisely to earn points for the House Cup— May the best house triumph!\n")
   
     for student in students:
        student.points = trivia_questions.trivia(student.name)
    
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

total_points = []
key_list = []
for key, value in house_points.items():
    if key != "muggle":
        total_points.append(value)
        key_list.append(key)
max_value = 1
for item in total_points:
    if item > max_value:
        max_value = item
max_index = total_points.index(max_value)
for item in total_points:
    if item > max_value:
        max_value = item
try:
    max_index = total_points.index(max_value)
    for item in total_points:
        if item > max_value:
            max_value = item
    max_index = total_points.index(max_value)
    try:
        item_index = total_points.index(max_value,(max_index +1))
        wizards = Wizarding_match(key_list[max_index],key_list[item_index])
        wizards.iteration()
        cup_winner = wizards.favorite 
    except ValueError:
        print(f'Hang on ... the judges are determining the winner')
    else:
        try:
            item2_index = total_points.index(max_value,(max_index +2))
            wizards2 = Wizarding_match(wizards.favorite,key_list[item2_index])
            wizards2.iteration() 
            cup_winner = wizards2.favorite
        except ValueError:
            print(f'Hang on .... the judges are determining the winner')
        else:
            try:
                item3_index = total_points.index(max_value,(max_index +3))
                wizards3 = Wizarding_match(wizards2.favorite,key_list[item3_index])
                wizards3.iteration()
                cup_winner = wizards3.favorite
            except ValueError:
                print(f'Hang on ..... the judges are determining the winner')
            else:
                print(f'Hang on ...... the judges are determining the winner')
except ValueError:
    print("None of the Hogwarts Houses Won :(")

print("\nSplendid work on the quiz, everyone! We've tallied the house points, and a champion has emerged.")
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

print("\nShall we unveil the final tally of points?")
y_n = ["yes", "no"]
while True:
          ans = input('\nrespond with a simple "yes" or "no." ').lower()
          if ans in y_n:
               break
          else:
               print("All that is required of you is to write 'yes' or 'no'—simple as a flick of a wand.")

if ans == "yes":
     for students in students:
          print(f"{students.name}: {students.points} points!") 

print("\nThat concludes our time together for now—until next year, take care and study well.")

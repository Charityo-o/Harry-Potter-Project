from student import Student 
import trivia_questions
import sorting_ceremony
from wizarding_match import Wizarding_match

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
all_points = G_points + S_points + R_points + H_points + m_points
house_points = {"Gryffindor": G_points, "Ravenclaw": R_points, "Slytherin": S_points, "Hufflepuff": H_points}
cup_winner = max(house_points, key = house_points.get)

if all_points == 0:
     print("None of the Hogwarts Houses Won :(")
else:
    for key, value in house_points.items():
        if key == "muggle":
            continue
        elif key == cup_winner: 
            continue
        elif value == house_points[cup_winner] and value != 0:
                wizards = Wizarding_match(key, cup_winner)
                wizards.iteration()
                cup_winner = wizards.favorite
    if house_points[cup_winner] < m_points:
        cup_winner == "muggle"
        muggle_tie = False
    elif house_points[cup_winner] == m_points:
        muggle_tie = True
    else: 
        muggle_tie = False

    print("\nSplendid work on the quiz, everyone! We've tallied the house points, and a champion has emerged.")
    if cup_winner == "muggle":
        print("Blimey! The Muggles have bested the wizards! You lot are getting full rides to Hogwarts — Potions, Charms, Herbology, even a peek at the Forbidden Forest!")
    elif muggle_tie == True:
        print(f"It appears that {cup_winner} and the Muggles are neck and neck — a most unexpected tie! Thus, the House Cup is awarded to {cup_winner}! And as for our clever Muggles, you shall be granted a grand tour of Hogwarts — mind the moving staircases!")
    else:
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

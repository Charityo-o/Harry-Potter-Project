from student import Student 

def sorting_ceremony():
    name = input("What is your name? ")
    S = 0
    G = 0
    R = 0
    H = 0
    m = 0
    print('Okay',name+', answer the following questions with "a", "b", "c", or "d".\nDo ensure your response is not in capital letters.')

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q1 = input()
    if q1 == 'a':
        S += 1
    elif q1 == 'b':
        G += 1
    elif q1 == 'c':
        R += 1
    elif q1 == 'd':
        H += 1
    else:
        m +=1
    
    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q2 = input()
    if q2 == 'a':
        S += 1
    elif q2 == 'b':
        G += 1
    elif q2 == 'c':
        R += 1
    elif q2 == 'd':
        H += 1
    else:
        m +=1
    
    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q3 = input()
    if q3 == 'a':
        S += 1
    elif q3 == 'b':
        G += 1
    elif q3 == 'c':
        R += 1
    elif q3 == 'd':
        H += 1
    else:
        m +=1
    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q4 = input()
    if q4 == 'a':
        S += 1
    elif q4 == 'b':
        G += 1
    elif q4 == 'c':
        R += 1
    elif q1 == 'd':
        H += 1
    else:
        m +=1
    
    print("\nWhich house do you believe you belong to?\na: Gryffindor\nb: Hufflepuff\nc: Ravenclaw\nd: Slytherin")
    q5 = input()
    if q5 == 'a':
        tie = "Gryffindor"
    elif q5 == 'b':
        tie = "Hufflepuff"
    elif q5 == 'c':
        tie = "Ravenclaw"
    elif q5 == 'd':
        tie = "Slytherin"
    else:
        tie = "muggle"

    if S > G and S > R and S > H and S > m:
        house = "Slytherin"
        return name, house
    elif G > S and G > R and G > H and G > m:
        house = "Gryffindor"
        return name, house
    elif R > G and R > S and R > H and R > m:
        house = "Ravenclaw"
        return name, house
    elif H > G and H > S and H > R and H > m:
        house = "Hufflepuff"
        return name, house
    elif  m > G and m > S and m > H and m > R:
        house = "muggle"
        print("You can't follow simple instructions, you must be a muggle.")
        return name, house
    else:
        if tie == "muggle":
            print("Really, you couldn't pick one... I guess you're a muggle.")
        return name, tie

def trivia(name):
    print("Okay", name+", trivia time!")
    points = 0
    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q1 = input()
    if q1 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q2 = input()
    if q2 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q3 = input()
    if q3 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q4 = input()
    if q4 == 'a':
        points += 1

        print("\nquestion and answers \na: \nb: \nc: \nd:")
    q5 = input()
    if q5 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q6 = input()
    if q6 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q7 = input()
    if q7 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q8 = input()
    if q8 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q9 = input()
    if q9 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q10 = input()
    if q10 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q11 = input()
    if q11 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q12 = input()
    if q12 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q13 = input()
    if q13 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q14 = input()
    if q14 == 'a':
        points += 1

    print("\nquestion and answers \na: \nb: \nc: \nd:")
    q15 = input()
    if q15 == 'a':
        points += 1
    return points

if __name__ == '__main__':
    num_users = int(input("How many fresh-faced young witches and wizards have joined our ranks this year? "))
    print("Let the Sorting Ceremony commence!")
    students = []
    for i in range (num_users):
        name, house= sorting_ceremony()
        s = Student(name, house)
        students.append(s)
        print(students)
        if house != "muggle":
            print(name, "you belong in...", house+"!")
        if i < num_users - 1:
            print("Would the next young wizard please step forward!")
    print("\nNow that all are sorted, it's time for a test of wit! Answer wisely to earn points for the House Cup—may the best house triumph!\n")
   
    for student in students:
        student.add_point = trivia(student.name)
    






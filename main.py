def sorting_ceremony():
    name = input("What is your name? ")
    S = 0
    G = 0
    R = 0
    H = 0
    m = 0
    print('Okay',name+', answer the following questions with "a", "b", "c", or "d".\nMake sure your answer is not capitalized.')

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
    
    print("\nWhat house would you like to be in?\na: Gryffindor\nb: Hufflepuff\nc: Ravenclaw\nd: Slytherin")
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



if __name__ == '__main__':
    num_users = int(input("How many new students are there this year? "))
    print("Let's begin the sorting ceremony.")
    user_dict = {}
    for i in range (num_users):
        name, house= sorting_ceremony()
        user_dict[name] = house
        print(name, "you belong in", house+"!")
        print(user_dict)


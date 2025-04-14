########
class Question:
    def __init__(self, ask, S, G, R, H):
        self.ask = ask
        self.S = S
        self.G = G
        self.R = R
        self.H = H

q1 = Question("\nquestion and answers \na: \nb: \nc: \nd:", 'a', 'b', 'c', 'd')
q2 = Question("\nquestion and answers \na: \nb: \nc: \nd:", 'a', 'b', 'c', 'd')
q3 = Question("\nquestion and answers \na: \nb: \nc: \nd:", 'a', 'b', 'c', 'd')
q4 = Question("\nquestion and answers \na: \nb: \nc: \nd:", 'a', 'b', 'c', 'd')
sorting_questions = [q1, q2, q3, q4]
q5 = Question("\nWhich house do you believe you belong to?\na: Gryffindor\nb: Hufflepuff\nc: Ravenclaw\nd: Slytherin", 'd', 'a', 'c', 'b')

def sorting_ceremony():
    name = input("What is your name? ")
    S = 0
    G = 0
    R = 0
    H = 0
    m = 0
    print('Okay',name+', answer the following questions with "a", "b", "c", or "d".\nDo ensure your response is not in capital letters.')
    
    for q in sorting_questions:
        print(q.ask)
        answer = input()
        if answer == q.S:
            S += 1
        elif answer == q.G:
            G += 1
        elif answer == q.R:
            R += 1
        elif answer == q.H:
            H += 1
        else:
            m += 1
        
    print(q5.ask)
    answer = input()
    if answer == q5.S:
            tie = "Slytherin"
    elif answer == q5.G:
            tie = "Gryffindor"
    elif answer == q5.R:
            tie = "Ravenclaw"
    elif answer == q5.H:
            tie = "Hufflepuff"
    else:
            tie = "muggle"
   
    houses = {"Hufflepuff": H, "Slytherin": S, "Gryffindor": G, "Ravenclaw": R, "muggle": m}
    winner = max(houses, key = houses.get)
    list = [H, S, G, R, m]
    list.sort()
    if list[3] == list[4]:
         if tie == "muggle":
              print("Really, you couldn't pick one... I guess you're a muggle.")
         return name, tie
    else: 
         if winner == "muggle":
              print("You can't follow simple instructions, you must be a muggle.")
         return name, winner

class Question:
    def __init__(self, ask, S, G, R, H):
        self.ask = ask
        self.S = S
        self.G = G
        self.R = R
        self.H = H

q1 = Question("\nWhat kind of legacy do you hope to leave? \na: I want to be remembered for standing up for what's right, no matter the cost.\nb: I want to leave behind a name that commands respect and won't be forgotten. \nc: I hope to be known for ideas that changed the way people think.\nd: I want people to say I made their lives better just by being there.", 'b', 'a', 'c', 'd')
q2 = Question("\nWhich of the following would you most hate people to call you? \na: Ordinary \nb: Cowardly \nc: Ignorant \nd: Selfish", 'a', 'b', 'c', 'd')
q3 = Question("\nOne of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. Now he has come top of the class in Charms, beating you into second place. Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson and asks you whether or not your classmate used a forbidden quill. What do you do? \na: Lie and say you don't know (but hope someone else tells the truth). \nb: Tell Professor Flitwick to ask your classmate, and warn your classmate to be honest. \nc: Tell him the truth. He gets what he gets. And since you are both in the same house, any points he loses will be regained by you anyway.\nd: Report it before the exam even starts.", 'c', 'd', 'b', 'a')
q4 = Question("\nA Muggle confronts you and says that they are sure you are a witch or wizard. Do you: \na: Ask what makes them think so. \nb: Agree, and ask whether they'd like a free sample of a jinx. \nc: Agree, and walk away, leaving them to wonder whether you are bluffing. \nd: Tell them that you are worried about their mental health, and offer to call a doctor.", 'c', 'b', 'a','d')
sorting_questions = [q1, q2, q3, q4]
q5 = Question("\nWhich house do you believe you belong to?\na: Gryffindor\nb: Hufflepuff\nc: Ravenclaw\nd: Slytherin", 'd', 'a', 'c', 'b')

def sorting_ceremony():
    name = input("What is your name? ")
    S = 0
    G = 0
    R = 0
    H = 0
    m = 0
    print('Okay',name+', answer the following questions with "a", "b", "c", or "d".')
    
    for q in sorting_questions:
        print(q.ask)
        answer = input().lower()
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

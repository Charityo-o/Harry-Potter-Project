class Quiz:
    def __init__(self, ask, answer):
        self.ask = ask 
        self.answer = answer

q1 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q2 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q3 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q4 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q5 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q6 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q7 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q8 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q9 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q10 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q11 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q12 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q13 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q14 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
q15 = Quiz("\nquestion and answers \na: \nb: \nc: \nd:", 'a')
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

def trivia(name):
    print("\nOkay", name+", trivia time!")
    points = 0
    for q in questions:
        print(q.ask)
        answer = input()
        if answer == q.answer:
            points += 1
        else:
            continue
    return points

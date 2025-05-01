class Quiz:
    def __init__(self, ask, answer):
        self.ask = ask 
        self.answer = answer

q1 = Quiz("\n1. question and answers \na: \nb: \nc: \nd:", 'a')
q2 = Quiz("\n2. question and answers \na: \nb: \nc: \nd:", 'a')
q3 = Quiz("\n3. question and answers \na: \nb: \nc: \nd:", 'a')
q4 = Quiz("\n4. question and answers \na: \nb: \nc: \nd:", 'a')
q5 = Quiz("\n5. What is the name of the Weasley family's house? \na: The Burrow \nb: The Cottage \nc: The Den \nd: The Nest", 'a')
q6 = Quiz("\n6. question and answers \na: \nb: \nc: \nd:", 'a')
q7 = Quiz("\n7. question and answers \na: \nb: \nc: \nd:", 'a')
q8 = Quiz("\n8. question and answers \na: \nb: \nc: \nd:", 'a')
q9 = Quiz("\n9. question and answers \na: \nb: \nc: \nd:", 'a')
q10 = Quiz("\n10. question and answers \na: \nb: \nc: \nd:", 'a')
q11 = Quiz("\n11. question and answers \na: \nb: \nc: \nd:", 'a')
q12 = Quiz("\n12. question and answers \na: \nb: \nc: \nd:", 'a')
q13 = Quiz("\n13. question and answers \na: \nb: \nc: \nd:", 'a')
q14 = Quiz("\n14. question and answers \na: \nb: \nc: \nd:", 'a')
q15 = Quiz("\n15. question and answers \na: \nb: \nc: \nd:", 'a')
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

valid_answers = {"a", "b", "c", "d"}

def trivia(name):
    print("\nOkay", name+", trivia time!")
    points = 0
    for q in questions:
        print(q.ask)
        while True:
            answer = input().lower()
            if answer in valid_answers:
                 break
            else:
                 print("The quill trembles with uncertainty—please choose a valid response: 'a', 'b', 'c', or 'd'.")
        if answer == q.answer:
            points += 1
        else:
            continue
    return points

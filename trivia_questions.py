class Quiz:
    def __init__(self, ask, answer):
        self.ask = ask 
        self.answer = answer

q1 = Quiz("\n1. What is the name of the first wizard his age Harry met? \na: Neville Longbottom \nb: Hermione Granger \nc: Ronald Weasley \nd: Draco Malfoy", 'c')
q2 = Quiz("\n2. What is the name of the first Goblin that greets Harry Potter at Gringotts bank? \na: Griphook \nb: Bogrod \nc: Ragnok \nd: Travers", 'a')
q3 = Quiz("\n3. What is the name of the magical creature that can only be seen by those who have witnessed death? \na: Hippogriff \nb: Thestral \nc: Acromantula \nd: Basilisk", 'b')
q4 = Quiz('\n4. In "Harry Potter and the Philosopher\'s Stone," what does Hagrid pull out of his coat to start the fire in the hut on the rock? \na: A dragon\'s tooth\nb: A pink umbrella \nc: A piece of Flobberworm mucus \nd: A fire-starting charm', 'b')
q5 = Quiz("\n5. What is the name of the Weasley family's house? \na: The Burrow \nb: The Cottage \nc: The Den \nd: The Nest", 'a')
q6 = Quiz("\n6. Who is the Half-Blood Prince? \na: Tom Riddle\nb: Severus Snape \nc: Harry Potter \nd: Albus Dumbledore", 'b')
q7 = Quiz("\n7. What is the name of the candy store near Hogwarts? \na: Zonko's \nb: Weasleys' Wizard Wheezes \nc: Honeydukes \nd: The Leaky Cauldron", 'c')
q8 = Quiz("\n8. What is the name of Hagrid's giant half-brother? \na: Grom \nb: Grunt \nc: Grog \nd: Grawp", 'd')
q9 = Quiz("\n9. What is the name of Hagrid's giant spider? \na: Shelob \nb: Fang \nc: Aragog \nd: Fluffy", 'c')
q10 = Quiz("\n10. What plant does Harry use to breathe underwater in the Triwizard Tournament? \na: Mandrake\nb: Devil's Snare\nc:  Wolfsbane \nd: Gillyweed", 'd')
q11 = Quiz("\n11. What type of dragon does Harry face in the first task of the Triwizard Tournament? \na: Hungarian Horntail \nb: Chinese Fireball\nc: Swedish Short-Snout \nd: Welsh Green", 'a')
q12 = Quiz("\n12. What potion grants good luck? \na: Polyjuice Potion \nb: Felix Felicis \nc: Amortentia \nd: Veritaserum", 'b')
q13 = Quiz("\n13. What is the name of the wizarding prison? \na: Azkaban \nb: Nurmengard \nc: Malfoy Manor \nd: The Forbidden Forest", 'a')
q14 = Quiz("\n14. What is the name of the wizarding newspaper based in London? \na: The Daily Prophet \nb: The Quibbler \nc: Witch Weekly\nd: The Wizard Times", 'a')
q15 = Quiz("\n15. (The final question) Who found Tom Riddle's diary? \na: Harry Potter \nb: Ron Weasley \nc: Hermione Granger\nd: Ginny Weasley", 'd')
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

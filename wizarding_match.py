class WrongAnswerError (Exception):
    def __init__(self, value):
        self.value = value
class Wizarding_match():
    def __init__(self,house1,house2):
        self.House1 = 0
        self.House2 = 0
        self.house1 = house1
        self.house2 = house2
        self.option1 = 'None'
        self.option2 = 'Nah'

    def winner(self):
        if self.House1 == 3:
            print(f'The winner is {self.house1}')
        elif self.House2 == 3:
            print(f'The winner is {self.house2}')
        else:
            return False
    def iteration(self):
        while self.winner() == False:
            try:
                print(f'{self.house1}, choose one of the following options: Rock, Paper, Scissors')
                self.option1 = input()
                if self.option1 not in ['Rock', 'Paper', 'Scissors']: 
                    raise WrongAnswerError(f'Your answer must be either: Rock, Paper, or Scissors') 
                print(f'{self.house2}, choose one of the following options: Rock, Paper, Scissors')
                self.option2 = input()
                if self.option2 not in ['Rock', 'Paper', 'Scissors']: 
                    raise WrongAnswerError(f'Your answer must be either: Rock, Paper, or Scissors')
                elif self.option1 == 'Rock' and self.option2 == 'Scissors':
                    self.House1 += 1
                elif self.option1 == 'Paper' and self.option2 == 'Rock':
                    self.House1 += 1 
                elif self.option1 == 'Scissors' and self.option2 == 'Paper':
                    self.House1 += 1 
                elif self.option1 == self.option2: 
                    print('You both picked the same spells? Lame')
                else:
                    self.House2 += 1
            except: 
                print("Error, Your answer must be either: Rock, Paper, or Scissors")

print("Welcome to the wizarding match, this shall determine which house has the best wizards!")
wizards = Wizarding_match('Ravenclaw', 'Hufflepuff')  
start = wizards.iteration()

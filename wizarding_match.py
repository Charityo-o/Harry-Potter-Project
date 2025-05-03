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
        self.favorite = 'Mip'
        print("There was a tie!\nTo determine the winner we'll have a wizarding match, this shall determine which house has the best wizards!")

    def winner(self):
        if self.House1 == 3:
            print(f'The winner is {self.house1}')
            self.favorite = self.house1
        elif self.House2 == 3:
            print(f'The winner is {self.house2}')
            self.favorite = self.house2
        else:
            return False

    def iteration(self):
        while self.winner() == False:
            try:
                print(f'{self.house1}, choose one of the following options: \nRock: a\nPaper: b\nScissors: c')
                #print(f'{self.house1}, choose one of the following options: Rock, Paper, Scissors')
                self.option1 = input()
                if self.option1 not in ['a', 'b', 'c']:
                #if self.option1 not in ['Rock', 'Paper', 'Scissors']: 
                    raise WrongAnswerError(f'Error! Your answer must be either: a (Rock), b (Paper), or c (Scissors)')
                    #raise WrongAnswerError(f'Error! Your answer must be either: Rock, Paper, or Scissors')
            except WrongAnswerError as wc_error: 
                print(wc_error)
            try:
               print(f'{self.house2}, choose one of the following options: \nRock: a\nPaper: b\nScissors: c') 
                #print(f'{self.house2}, choose one of the following options: Rock, Paper, Scissors')
                self.option2 = input()
                if self.option2 not in ['a', 'b', 'c']:
                #if self.option2 not in ['Rock', 'Paper', 'Scissors']: 
                    raise WrongAnswerError(f'Error! Your answer must be either: a (Rock), b (Paper), or c (Scissors)')
                    #raise WrongAnswerError(f'Error! Your answer must be either: Rock, Paper, or Scissors')
            except WrongAnswerError as wc_error: 
                print(wc_error)
            finally: self.points()
                
    def points(self):
        if self.option1 == 'a' and self.option2 == 'c':
        #if self.option1 == 'Rock' and self.option2 == 'Scissors':
            self.House1 += 1
        elif self.option1 == 'b' and self.option2 == 'a':
        #elif self.option1 == 'Paper' and self.option2 == 'Rock':
            self.House1 += 1 
        elif self.option1 == 'c' and self.option2 == 'b':
        #elif self.option1 == 'Scissors' and self.option2 == 'Paper':
            self.House1 += 1
        elif self.option1 in ['a', 'b', 'c'] and self.option2 not in ['a', 'b', 'c']:
        #elif self.option1 in ['Rock', 'Paper', 'Scissors'] and self.option2 not in ['Rock', 'Paper', 'Scissors']:
            self.House1 += 1
        elif self.option1 == self.option2: 
            print('You both picked the same spells? Lame')
        else:
            self.House2 += 1
        


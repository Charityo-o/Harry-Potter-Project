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
        print("There was a tie!\nTo determine the winner we'll have a wizarding match \nThis shall determine which house has the best wizards!")

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
                self.option1 = input()
                if self.option1 not in ['a', 'b', 'c']: 
                    raise WrongAnswerError(f'Error! Your answer must be either: a (Rock), b (Paper), or c (Scissors)')
            except WrongAnswerError as wc_error: 
                print(wc_error)
                continue
            try:
               print(f'{self.house2}, choose one of the following options: \nRock: a\nPaper: b\nScissors: c') 
               self.option2 = input()
               if self.option2 not in ['a', 'b', 'c']:
                    raise WrongAnswerError(f'Error! Your answer must be either: a (Rock), b (Paper), or c (Scissors)')
            except WrongAnswerError as wc_error: 
                print(wc_error)
                continue
            finally: self.points()
                
    def points(self):
        if self.option1 == 'a' and self.option2 == 'c':
            self.House1 += 1
        elif self.option1 == 'b' and self.option2 == 'a':
            self.House1 += 1 
        elif self.option1 == 'c' and self.option2 == 'b':
            self.House1 += 1
        elif self.option1 in ['a', 'b', 'c'] and self.option2 not in ['a', 'b', 'c']:
            self.House1 += 1
        elif self.option1 == self.option2: 
            print('You both picked the same spells? Lame')
        else:
            self.House2 += 1
        


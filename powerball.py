from random import randint
# Name: Bizuayehu Belete


class List():
    def __init__(self):
        self.user_numbers = []
        self.user_powerball = []



    def num1(self):
        for i in range(1):
            powerball =randint(1,10)
            self.user_powerball.append(powerball)
              # Check if this number has already been picked and ...
            while powerball in self.user_numbers :
             # ... if it has, pick a new number instead
             powerball = randint(1, 20)

        # Initialise an empty list that will be used to store the 5 lucky numbers!
        for i in range(0, 5):
            number = randint(1, 20)
            # Now that we have a unique number, let's append it to our list.
            self.user_numbers.append(number)
            # Check if this number has already been picked and ...
            while number in self.user_numbers :
             # ... if it has, pick a new number instead
             number = randint(1, 20)
             # Sort the list in ascending order
             self.user_numbers.sort()



class Setup(List):
    def __init__(self):
        super().__init__()
        self.Luckyball_numbers = []
        self.Luckyballs = []

    def num(self):
        for num in range(0, 5):
            user_num = randint(1, 20)
            self.Luckyball_numbers.append(user_num)
        power_ball = randint(1, 5)
        self.Luckyballs.append(power_ball)
        self.Luckyball_numbers.sort()


class Condition(Setup):
  def Condition(self):
    self.correct = 0
    for i in self.user_numbers:
        if i in self.Luckyball_numbers:
         self.correct+=1

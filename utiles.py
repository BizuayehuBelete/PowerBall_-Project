from powerball import *
import color

class If_Condition(Condition):
    def test(self,Conditon):
        print(f'\n\33[1mToday’s Powerball Winning Numbers : \33[0m' + color.MAGENTA + f"{self.user_numbers}", color.YELLOW + f'{self.user_powerball}')
        print(color.RESET+f'\33[1mYour Lucky Numbers:\33[1m' + color.MAGENTA + f"{self.Luckyball_numbers}",
              color.YELLOW + f' {self.Luckyballs}')
        if self.user_powerball == self.Luckyballs and self.correct == 5:
                print(" Correct White Balls and The Powerball:$324,000,000 ")
        elif  self.user_powerball == self.Luckyballs and self.correct == 5:
             print(" 5 Correct White Balls, But NO Powerball:$1,000,000 ")
        elif  self.user_powerball ==self.Luckyballs and self.correct == 4:
                print(" 4 Correct White Balls And The Powerball: $10,000 ")
        elif self.user_powerball != self.Luckyballs and self.correct== 4:
             print("4 Correct White Balls, But no Powerball: $100 ")
        elif self.user_powerball ==self.Luckyballs and self.correct== 3:
                print("3 Correct White Balls And  Powerball:$100")
        elif self.user_powerball != self.Luckyballs and  self.correct== 3:
             print("3 Correct White Balls, But No Powerball:$7")
        elif self.user_powerball != self.Luckyballs and self.correct== 2:
                print("2 Correct White Balls And NO  Powerball:$6")
        elif self.user_powerball == self.Luckyballs and self.correct== 2:
                print("2 Correct White Balls And  Powerball:$7")
        elif self.user_powerball != self.Luckyballs and self.correct== 1:
                print("1 Correct White Ball And NO  Powerball:$3")
        elif self.user_powerball==self.Luckyballs and self.correct== 1:
                print("1 Correct White Ball And  Powerball:$4")
        elif self.user_powerball ==self.Luckyballs and self.correct== 0:
                print("No White Balls, Just The Powerball: $4")
        elif self.user_powerball != self.Luckyballs and self.correct== 0:
             print("Please, Try Again!” ")

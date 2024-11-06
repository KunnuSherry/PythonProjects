import random
choices = [1,2,3]
print("1-stone, 2-paper, 3-scissors, 4-quit")
userChoice =0
def game(userChoice, compChoice):
      print(f'User Choosed: {userChoice}')
      print(f'Computer Choosed: {compChoice}')
      
      if(userChoice==compChoice):
            return "draw"
      elif userChoice ==1:
            if compChoice ==3:
                  return "User Won"
            else:
                  return "Computer Won"
      elif userChoice ==2:
            if compChoice ==1:
                  return "User Won"
            else:
                  return "Computer Won"
      elif userChoice ==3:
            if compChoice ==2:
                  return "User Won"
            else: 
                  return "Comp Won"


while(userChoice!=4):
      userChoice = int(input('Enter your choice: '))
      compChoice = random.choice(choices)
      print(game(userChoice, compChoice))


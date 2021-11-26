from random import randint 

tie = 0
win = 0 
lose = 0

def main():
  games = int(input("How many games would you like to play?"))
  while games > 0:
    games -= 1
    comp = computer()
    choice = user()
    print("You played", choice, "and the computer played", comp)
    winner(comp, choice)



def computer():
  # CORRECTION: randint in range (0,3) always return FALSE. BELOW IS THE CORRECT WAY
  comp = randint(0, 2)
  if comp == 0:
    comp = 'rock'
  elif comp == 1:
    comp = 'paper'
  elif comp == 2:
    comp = 'scissors'
  return comp

def user():
  choice = int(input("choose 0 for rock, 1 for paper, or 2 for scissors: "))
  if choice == 0:
    choice = 'rock'
  elif choice == 1:
    choice = 'paper'
  elif choice == 2:
    choice = 'scissors'
  else:
    print("invalid input")
  return choice


def winner(comp, choice):  
  # CORRECTION: MAKE ALL THE COUNTERS GLOBAL
  global tie
  global win
  global lose 

  while True:
    if choice == "rock" and comp == "rock":
      result = 'tie'
      tie += 1
      break
    elif choice == 'rock'and comp == 'scissors':
      result = "you win"
      win += 1
      break
    elif choice == 'rock' and comp == 'paper':
      result = "you lose"
      lose += 1
      break
    elif choice == 'paper' and comp == 'paper':
      result = 'tie'
      tie += 1
      break
    elif choice == 'paper' and comp == 'scissors':
      result = 'you lose'
      lose += 1
      break
    elif choice == 'paper' and comp == 'rock':
      result = 'you win'
      # CORRECTION: ITS NOT =+ ITS +=
      # win =+ 1
      win += 1
      break
    elif choice == 'scissors' and comp == 'scissors':
      result = 'tie'
      tie += 1
      break
    elif choice == 'scissors' and comp == 'paper':
      result = 'you win'
      win += 1
      break
    elif choice == 'scissors' and comp == 'rock':
      result = 'you lose'
      lose +=1
      break
    else:
      print("error")
      break
  print(result)      


main()
print("you won", win,"times, and lost", lose,"times, and tied", tie,"times.")
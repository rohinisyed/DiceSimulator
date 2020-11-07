from random import randint 

play_game = True 

while play_game: 
  dice_roll = randint(1,6)
  print ("The dice has rolled:",dice_roll)
  play_again = input ("Do you want to roll again? N to stop: ") #I PUT Y
  if play_again == "N":
    play_game = False    
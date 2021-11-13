print("Rock Paper Scissors, offline.")
from random import choice
def game():
  rps = ["scissors","paper","rock"]
  rockpaperscissors = input("Rock, paper or scissors? ").lower()
  if rockpaperscissors != "rock" and rockpaperscissors != "paper" and rockpaperscissors != "scissors":
    print("Please enter rock, paper or scissors.")
    game()
  airps = choice(rps)
  print(f"""AI chooses: {airps}
Player chooses: {rockpaperscissors}""")
  if airps == rockpaperscissors:
    print("Tie!")
  else:
    if airps == "rock" and rockpaperscissors == "paper":
      print("Player wins!")
    elif airps == "paper" and rockpaperscissors == "scissors":
      print("Player wins!")
    elif airps == "scissors" and rockpaperscissors == "rock":
      print("Player wins!")
    else: 
      print("AI wins!")
  def loop():
    exit = input("Do you want to exit? Type 'Y' or 'N'. ").upper()
    if exit == "Y":
      print("Ok!")
      from sys import exit
      exit(0)
    elif exit == "N":
      print("Ok!")
      game()
    else:
      print("Please enter a valid option.")
      loop()
  loop()
game()

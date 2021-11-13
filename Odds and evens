import sys
import random
print("Odds and Evens, offline.")
def game():
  try:
    G = int(input("What number from 1 to 5? "))
  except ValueError:
    print("Please choose a number.")
    game()
  if G > 5 or G < 1:
    print("Please enter a number from 1-5.")
    game()
  GEO = input("Odd or Even? ").lower()
  if GEO != "odd" and GEO != "even":
    print("Please enter 'Odd' or 'Even'.")
    game()
  AIG = random.randint(1,5)
  AIGEO = random.randint(1,2)
  if AIGEO == 1:
    AIGEO = "even"
  else:
    AIGEO = "odd"
  Total = G+AIG
  print(f"""AI Number: {AIG}
AI Guess: {AIGEO}
Total of both Numbers: {Total}""")
  if Total == 2 or Total == 4 or Total == 6 or Total == 8 or Total == 10:
    WhatToExpect = "even"
  else:
    WhatToExpect = "odd"
  if AIGEO == WhatToExpect and GEO == WhatToExpect:
    print("Tie!")
  elif AIGEO == WhatToExpect:
    print("AI Wins!")
  elif GEO == WhatToExpect:
    print("Player Wins!")
  else:
    print("Nobody wins!")
  def loop():
    exit = input("Would you like to play again? ('Y' or 'N') ").upper()
    if exit == "Y":
      print("Okay! Restarting...")
      game()
    elif exit == "N":
      print("Okay! Exiting...")
      sys.exit(0)
    else:
      print("Please enter a valid option.")
      loop()
  loop()
game()

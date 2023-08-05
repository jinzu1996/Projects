import random





def get_choice():
  player_choice = input("Enter a choice (rock, paper, scissors):")
  option = ["rock","paper","scissors"]
  computer_choice = random.choice(option)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def chk_wins(player,computer):
  print(f"you choose {player}, player choose {computer} ")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "scissors cut paper! You lose." 
  elif player == "scissors":
    if computer == "paper":
      return "scissors cut paper! You win!"
    else:
      return "Rock smashes scissors!! You lose."    
    
choices = get_choice()
result = chk_wins(choices["player"],choices["computer"])
print(result)

import random
choices = ["Rock","Paper","Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player= input("Rock,paper or Scissors?").capitalize()
    #conditions of Rock,paper and scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "paper":
            print("you lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("you win!",player,"smashes",computer)
            player_score+=1
    elif player == "paper":
        if computer == "scissors":
            print("you lose!",computer,"cut",player)
            cpu_score+=1
        else:
            print("you win!",player,"covers",computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"cpu:{cpu_score}")
        print(f"plaer:{player_score}")
        break
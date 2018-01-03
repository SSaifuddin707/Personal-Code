print("\n\t\t\tRock Paper Scissors")
def RPS():
    
    player1 = input("\nPlayer 1 input your turn\n")

    player2 = input("\nPlayer 2 input your turn\n")
    if (player1 == player2):
        print("Tie!")
        RPS()
    elif (player1 == "rock") and (player2 == "paper"):
        print("Player 2 wins with paper!")
    elif (player1 == "paper") and (player2 == "rock"):
        print("Player 1 wins with paper!")
    elif (player1 == "rock") and (player2 == "scissors" or "scissor"):
        print("Player 1 wins with rock!")
    elif (player1 == "scissors" or "scissor") and (player2 == "rock"):
        print("Player 2 wins with rock!")
    elif (player1 == "scissors" or "scissor") and (player2 == "paper"):
        print("Player 1 wins with scissors!")
    elif (player1 == "paper") and (player2 == "scissors" or "scissor"):
        print("Player 2 wins with scissors!")
RPS()

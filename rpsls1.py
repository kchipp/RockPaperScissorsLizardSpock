

def playerOne():
    playerOneChoice = input("Player One Make Your Choice ")
    playerOneChoice = playerOneChoice.lower()
    isValidChoice = validateChoice(playerOneChoice)
    if isValidChoice == True:
        return playerOneChoice
    elif isValidChoice == False:
        print("Please enter a valid choice")
        return playerOne()
        
def playerTwo():
    playerTwoChoice = input("Player Two Make Your Choice ")
    playerTwoChoice = playerTwoChoice.lower()
    isValidChoice = validateChoice(playerTwoChoice)
    if isValidChoice == True:
        return playerTwoChoice
    elif isValidChoice == False:
        print ("Please enter a valid choice")
        return playerTwo()
    
def validateChoice(playerChoice):
    if playerChoice == "rock" or playerChoice == "scissors" or playerChoice == "paper" or playerChoice == "spock" or playerChoice == "lizard":
        return True
    else:
        return False    
    
def rpsls(playerOneChoice, playerTwoChoice, scores):
    if playerOneChoice == "rock" and playerTwoChoice == "scissors":
        print ("Player One Wins")
        scores[0] += 1
    elif playerOneChoice == "rock" and playerTwoChoice == "lizard":
        print ("Player One Wins")
        scores[0] += 1
    elif playerOneChoice == "paper" and playerTwoChoice == "rock":
        print ("Player One Wins")
        scores[0] += 1
    elif playerOneChoice == "paper" and playerTwoChoice == "spock":
        print ("Player One Wins")
        scores[0] += 1
    elif playerOneChoice == "scissors" and playerTwoChoice == "paper":
       print ("Player One Wins")
       scores[0] += 1
    elif playerOneChoice == "scissors" and playerTwoChoice == "lizard":
       print ("Player One Wins")
       scores[0] += 1
    elif playerOneChoice == "lizard" and playerTwoChoice == "paper":
        print ("Player One Wins")
        scores[0] += 1        
    elif playerOneChoice == "lizard" and playerTwoChoice == "spock":
        print ("Player One Wins")
        scores[0] += 1
    elif playerOneChoice == "spock" and playerTwoChoice == "scissor":
        print ("Player One Wins")
        scores[0] += 1        
    elif playerOneChoice == "spock" and playerTwoChoice == "rock":
        print ("Player One Wins")
    elif playerOneChoice == "rock" and playerTwoChoice == "spock":  
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "rock" and playerTwoChoice == "paper":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "paper" and playerTwoChoice == "lizard":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "paper" and playerTwoChoice == "scissors":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "spock" and playerTwoChoice == "paper":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "scissors" and playerTwoChoice == "rock":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "spock" and playerTwoChoice == "lizard":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "lizard" and playerTwoChoice == "scissors":
        print ("Player Two Wins")
        scores[1] += 1
    elif playerOneChoice == "scissors" and playerTwoChoice == "rock":
        print ("Player Two Wins")
        scores[1] += 1
    else:
        print ("Players Have Tied")

def chooseReplay():
    choice = input("Do you want to play again? ")
    if choice.lower() in ["no", "n"]:
        return False
    else:
        return True
            
def main():
    print ("Welcome to Rock, Paper, Scissors, Lizard, Spock")
    replay = True
    scores = [0, 0]
    while replay:
        OneChoice = playerOne()
        TwoChoice = playerTwo()
        rpsls(OneChoice, TwoChoice, scores)
        print (scores)
        replay = chooseReplay()
        
    
if __name__ == "__main__":
    main()
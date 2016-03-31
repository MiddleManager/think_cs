import random

# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """

    rng = random.Random()

    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))

    return result

def main():
    play_again = "y"
    scoreboard = [0, 0, 0, 0] # loss, tie, win, total
    turn = True

    while (play_again == "y"):
        scoreboard[3] += 1 # total amount of games

        # Main function that plays the game
        who = play_once(turn)

        # Switch turn
        if (turn):
            turn = False
        else:
            turn = True

        # Calculates the results and prints them
        if (who == -1):
            print("You lost!")
            scoreboard[0] += 1
        elif (who == 0):
            print("You tied!")
            scoreboard[1] += 1
        else:
            print ("You won!")
            scoreboard[2] += 1

        player_perc = scoreboard[2] / (scoreboard[3] - scoreboard[1])
        player_perc = int(player_perc * 100)

        print("Scoreboard:" +
              "\nLosses: " + str(scoreboard[0]) +
              " Ties: " + str(scoreboard[1]) +
              " Wins: " + str(scoreboard[2]) +
              " Games: " + str(scoreboard[3]) +
              " Percentage: " + str(player_perc) + "%")

        print("Play again: (y - n)")
        play_again = input()

    print("Goodbye!")

main()

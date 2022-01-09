# Prompt
# Allow the user to input their question.
# Show an in progress message.
# Create 5 to 10 responses, and show a random response.
# Allow the user to ask another question/advice or quit the game.

from time import sleep
from random import choice
# the above imports sleep for the in progress message, choice for the responses


def eight_ball():
    input("What's your question? ")
    print("Thinking...")
    sleep(2)
    response = ["Yes", "No", "Of Course", "Never", "Ask Later", "Don't Count on it", "I'm Hungry"]
    print(choice(response))
# the function above asks question, shows in progress message and gives response


eight_ball()
# above calls function


def again():
    another = input("Another Question? ")
    if another.lower() == "yes":
        eight_ball()
        again()
    elif another.lower() == "no":
        quit_game = input("Quit Game? ")
        if quit_game.lower() == "yes":
            print("Bye, thanks for playing the Magic 8 Ball")
        elif quit_game.lower() == "no":
            eight_ball()
            again()
# function above is the play again system, if yes for another question eight ball restarts
# if no, quit game appears, if quit game is yes then game stops
# if quit game is no then eight ball restarts.


again()

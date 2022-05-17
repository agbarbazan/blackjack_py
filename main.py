from art import logo
from controller.Game import Game

print(logo)
while True:
    user_input = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
    if user_input == 'y':
        game = Game()
        game.play()
    elif user_input == 'n':
        break




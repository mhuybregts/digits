import sys
import keyboard

from digits import Digits

if __name__ == "__main__":

    def pad_line():
        sys.stdout.write("\033[K")

    print("Welcome to Digits!")
    print("You will be a shown a digit from 0 to 9")
    print("You can save a digit by pressing S")
    print("You can match a digit by pressing M")
    print("You score points by matching digits")
    print("Once you successfully match a digit, you have to"
          "save it the next time you see it")
    print("If you save the same digit twice in a row, or "
          "match a digit before saving it, the game is over")

    game = Digits()
    game_over = False

    while not game_over:

        next_digit = game.get_digit()
        sys.stdout.write(f"\nThe next digit is: {next_digit}, "
                         "what do you want to do? (S or M)")

        while True:
            action = keyboard.read_event()
            if keyboard.is_pressed('s'):
                if not game.save(next_digit):
                    game_over = True
                    sys.stdout.write("\nOops! You saved a digit that you "
                                     "should have matched\n")
                else:
                    sys.stdout.write("\rSaved a digit")
                    pad_line()
                break

            elif keyboard.is_pressed('m'):
                if not game.match(next_digit):
                    game_over = True
                    sys.stdout.write("\nOops! You matched a digit that you "
                                     "should have saved\n")
                else:
                    sys.stdout.write("\rMatched a digit")
                    pad_line()
                break

    print(f"Game Over\nYou got a score of {game.score}")

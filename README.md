# digits

A simple yet addictive memory game

## Rules

Digits is a straightforward game that tests your memory. When the game begins,
a player is shown a digit from 0-9. If the player has not seen the digit, they
save it. It they have previously saved the digit, they should match it.

After matching a digit, the player should save that digit the next time
they see it. If a player saves a digit that they should have matched or matches
a digit that they should have saved, the game is over.

Evertime a player matches a digit, they score a point. The game will keep a history
of when you matched and saved, but it will not tell you which digit.

## How to play

### CLI

Run [digits_cli.py](/digits_cli.py) and do the following

- Press 's' when you want to save a digit
- Press 'm' when you want to match a digit

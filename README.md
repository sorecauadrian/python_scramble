# unscrambling game

## overview
this project represents my solution to the final exam for the fundamentals of programming course at my university. it is a console-based game with the following structure:
- the user receives a scrambled sentence where the whitespaces, the first letter of each word, and the last letter of each word retain their initial positions
- the user swaps pairs of letters until he arrives at the intial sentence
- if the user remains without moves, then they lose
- the fewer swaps the user makes, the higher their score will be

## features
- built using layered architecture
- the initial sentence (unscrambled) is chosen randomly from a text file
- the sentence is scrambled randomly, but without breaking the rules stated above
- the commands inputed by the user are interpreted by the program
- if a command is invalid, then the program raises an exception and the user is notified
- the user is able to undo the last operation

## gameplay
![Screenshot from 2023-12-03 23-08-59](https://github.com/sorecauadrian/unscrambling_game/assets/79454929/271f015c-f1c7-4275-acfd-4bcd71794b4c)

![Screenshot from 2023-12-03 23-12-59](https://github.com/sorecauadrian/unscrambling_game/assets/79454929/4f826478-46d6-4921-89ba-4b1b26008537)

# project---dragon-game---text-base-game

Dragon Cave Adventure Game

This Python script is a simple text-based adventure game where the player explores a kingdom of dragons. The player must choose one of five caves, hoping to find the friendly dragon who will share his treasure. However, most of the caves contain hungry dragons that will eat the player on sight!

Features

Random Cave Selection: Uses the random module to randomly select which cave contains the friendly dragon.
Suspenseful Gameplay: Utilizes the time module to add delays, building suspense as the player approaches the chosen cave.
File Handling: Employs the os module to handle file operations, such as saving the result of the last game to a text file.

How to Play

Run the script.
Follow the prompts to choose a cave (1, 2, 3, 4, or 5).
Discover if you found the friendly dragon or got eaten by a hungry one.
Decide if you want to play again.

Code Overview

display_intro(): Displays the introduction text.
choose_cave(): Prompts the player to choose a cave.
check_cave(chosen_cave): Checks if the chosen cave has the friendly dragon and displays the result.
save_result(result): Saves the result of the last game to a text file.
main(): Runs the game loop, allowing the player to play multiple times.

Enjoy your adventure in the Kingdom of Dragons!

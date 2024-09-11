import random  # Importing the random module to generate random numbers
import time  # Importing the time module to add delays for suspense
import os  # Importing the os module to handle file operations

# Function to display the introduction text
def display_intro():
    print("You are in the Kingdom of Dragons. In front of you,")
    print("you see five caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragons")
    print("are hungry and will eat you on sight!")

# Function to let the player choose a cave
def choose_cave():
    cave = ""
    # Loop until the player chooses a valid cave (1, 2, 3, 4, or 5)
    while cave not in ["1", "2", "3", "4", "5"]:
        print("Which cave will you go into? (1, 2, 3, 4, or 5)")
        cave = input()
    return cave  # Return the player's choice

# Function to check if the chosen cave has the friendly dragon
def check_cave(chosen_cave):
    print("You approach the cave...")
    time.sleep(2)  # Wait for 2 seconds to build suspense
    print("It is dark and spooky...")
    time.sleep(2)  # Wait for 2 more seconds
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)  # Final pause before revealing the outcome

    friendly_cave = random.randint(1, 5)  # Randomly select a cave to be the friendly one

    # Check if the chosen cave is the friendly one
    if chosen_cave == str(friendly_cave):
        print("Gives you his treasure!")
        return "Friendly"  # Return "Friendly" if the player wins
    else:
        print("Gobbles you down in one bite!")
        return "Hungry"  # Return "Hungry" if the player loses

# Function to save the result of the last game to a text file
def save_result(result):
    with open("last_game_result.txt", "w") as file:  # Open the file in write mode
        file.write(f"Last game result: {result}\n")  # Write the result to the file

# Main function to run the game
def main():
    # Clear the file at the start of the program to ensure it's empty on each run
    open("last_game_result.txt", "w").close()

    play_again = "yes"  # Initialize the play_again variable to "yes"
    while play_again.lower() in ["yes", "y"]:  # Loop as long as the player wants to play again
        display_intro()  # Display the introduction
        cave_number = choose_cave()  # Get the player's chosen cave
        result = check_cave(cave_number)  # Check the outcome of the chosen cave
        save_result(result)  # Save the result to the text file
        print("Do you want to play again? (yes or no)")  # Ask if the player wants to play again
        play_again = input()  # Get the player's response
    print("Thank you for playing!")  # Print a thank you message when the game ends

main()  # Call the main function to start the game

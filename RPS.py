# TASK - 3
# ROCK PAPER SCISSORS

from ipywidgets import widgets
from IPython.display import display
import random

# Function to play Rock, Paper, Scissors
def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = f"Computer chose {computer_choice}. "

    if user_choice == computer_choice:
        result += "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result += "You win!"
    else:
        result += "Computer wins!"

    result_label.value = result

# Create widgets
rock_button = widgets.Button(description="Rock")
paper_button = widgets.Button(description="Paper")
scissors_button = widgets.Button(description="Scissors")
result_label = widgets.Label(value="")

# Assign functions to buttons
rock_button.on_click(lambda b: play_game('Rock'))
paper_button.on_click(lambda b: play_game('Paper'))
scissors_button.on_click(lambda b: play_game('Scissors'))

# Display widgets
display(widgets.HBox([rock_button, paper_button, scissors_button]))
display(result_label)

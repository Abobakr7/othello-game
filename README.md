# Othello Game with Python Tkinter

This project is a Python implementation of the classic board game Othello using the Tkinter GUI library. It supports two gameplay modes: player vs. player (1vs1) and player vs. computer (1 vs. computer), with the computer's difficulty adjustable between easy, medium, and hard levels.

## Features

-   **1vs1 Mode**: Play against another human player.
-   **1 vs. Computer Mode**: Play against an AI with three difficulty levels: Easy, Medium, and Hard.
-   **Graphical User Interface**: Built with Tkinter for an intuitive and user-friendly experience.
-   **Move Validation**: Ensures all moves adhere to Othello rules.

## Project Structure

The project is organized into the following directories:

-   **Model**: Contains files related to the game board and its logic.

    -   `Board.py`: Responsible for creating and managing the game board.

-   **Controller**: Manages the game logic and AI.

    -   `Othello.py`: Handles the core game logic.
    -   `AI.py`: Implements the AI agent for playing against a human.

-   **View**: Contains the graphical user interface components.

    -   `GameGUI.py`: Responsible for building and managing the game’s GUI.

-   **Utils**: Provides utility functions and constants.

    -   `Constants.py`: Contains constant variables used throughout the project.

-   **assets**: contains images that would be used in the game

## Installation

To set up and run the Othello game, follow these steps:

### Steps

1. **Clone the Repository**

    ```
    git clone https://github.com/Abobakr7/othello-game.git
    ```

2. **Navigate to the Project Directory**

    ```
    cd othello-game
    ```

3. **Install Dependencies**

    If you need any additional Python packages, install them using `pip`. For this project, no external packages are required beyond Tkinter and Numpy.

    ```
    pip install -r requirements.txt
    ```

4. **Run the Game**

    Launch the game by executing the Python script:

    ```
    python main.py
    ```

## Usage

1. **Start the Game**

    After running the script, the game window will open.

2. **Choose a Game Mode**

    - **1vs1**: Select this option to play against another human player.
    - **1 vs. Computer**: Choose this option to play against the AI. You can select the difficulty level (Easy, Medium, or Hard) from the menu.

3. **Play the Game**

    - Click on the board to place your pieces.
    - The game will automatically validate your moves and update the board accordingly.
    - Follow the on-screen instructions for each move and to view game status.

4. **End of Game**

    The game will declare the winner and provide options to start a new game or exit.

## Acknowledgments

-   Tkinter for providing a straightforward way to create GUIs in Python.
-   [Othello Game Rules](https://en.wikipedia.org/wiki/Reversi) for the game mechanics.

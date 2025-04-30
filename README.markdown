# Sudoku Solver

**Sudoku Solver** is an interactive application that combines the classic Sudoku game with augmented reality (AR) technology. It allows users to play Sudoku, solve puzzles manually or automatically, and experience real-time puzzle solving through AR. The project leverages machine learning to extract Sudoku puzzles from images or live camera feeds and employs the efficient Exact Cover method to solve them.

## Features

- **User-Friendly GUI**: Intuitive interface for seamless navigation and interaction.
- **Augmented Reality Integration**: Real-time Sudoku solving with AR overlay.
- **Manual and Automatic Solving**: Solve puzzles yourself or let the application do it for you.
- **Puzzle Import**: Load Sudoku puzzles from image files or capture them via camera.
- **Interactive Experience**: Engage with both game and AR features effortlessly.

## Installation

To set up and run the Sudoku Solver application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sudoku-solver.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd sudoku-solver
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Launch the Application**: Execute `main.py` to start the program.
2. **Main Menu**: Select either "Play Sudoku" or "AR Sudoku" to begin.
3. **Playing Sudoku**:
   - Choose "Play Sudoku" to start a game.
   - Input numbers manually or import a puzzle from an image or camera.
   - Solve it yourself or click "Solve" for an automatic solution.
4. **Augmented Reality Mode**:
   - Select "AR Sudoku" to use the AR feature.
   - Aim your camera at a Sudoku puzzle to see the solution overlaid in real-time.
5. **Return to Menu**: Use the "Back" button to return to the main menu anytime.

## Technology Used

- **Programming Language**: Python
- **Machine Learning**: Extracts Sudoku puzzles from images and camera feeds.
- **Solving Algorithm**: Exact Cover method for efficient, deterministic solving.
- **Augmented Reality**: Enables real-time solution visualization.

## Why Exact Cover Method?

The Exact Cover method stands out for solving Sudoku due to:
- **Efficiency**: Quickly handles complex puzzles.
- **Determinism**: Guarantees a solution if one exists, without guesswork.
- **No Backtracking**: Avoids trial-and-error for faster results.
- **Versatility**: Applicable to various combinatorial problems.
- **Educational Value**: Offers insight into algorithm design.

## Future Scope

The project aims to evolve into a comprehensive puzzle-solving platform, including:
- Rubik's Cube solver
- Crossword puzzles
- Jigsaw puzzles
- Brain teasers

These additions will cater to diverse puzzle enthusiasts, enhancing problem-solving skills and enjoyment.

## Contributing

We welcome contributions! To get involved:
1. **Fork the Repository**: Create your own fork of the project.
2. **Create a Branch**: Work on a new branch for your changes.
3. **Make Changes**: Commit your updates with clear messages.
4. **Submit a Pull Request**: Propose your changes for review.

Adhere to the project's coding standards for smooth collaboration.

## License

This project is released under the [MIT License](LICENSE).

## Contact

For questions, feedback, or support:
- **Email**: [your.email@example.com](mailto:your.email@example.com)
- **GitHub**: [yourusername](https://github.com/yourusername)
# 🎮 Tic-Tac-Toe User Guide

## Game Overview
Tic-Tac-Toe is a classic two-player game where players take turns marking spaces on a 3x3 grid. The player who succeeds in placing three of their marks (X or O) in a horizontal, vertical, or diagonal row wins the game.

## Getting Started
1. Launch the game by running `python main.py`
2. Click the "Start Game" button on the welcome screen to begin

## Game Interface
- **Score Display**: At the top of the screen, showing X wins, O wins, and draws
- **Game Grid**: The 3x3 playing field in the center
- **Game Over Screen**: Appears when a game ends, showing the winner or draw

## How to Play
1. **Player Turns**:
   - Player X goes first (marked in green)
   - Player O goes second (marked in brown)
   - Players alternate turns until the game ends

2. **Making Moves**:
   - Click any empty cell to place your mark
   - Once placed, a mark cannot be changed
   - Invalid moves are automatically rejected

3. **Winning the Game**:
   - Get three of your marks in a row (horizontal, vertical, or diagonal)
   - The game ends immediately when a player wins
   - If no player wins and all cells are filled, the game is a draw

## Controls
- **Mouse**: Click to place X/O
- **R key**: Restart the current game
- **Q key**: Quit the application

## Game Features
- Real-time score tracking
- Clear game-over messages
- Easy restart option
- Clean, minimalist design

## Tips for Playing
1. Try to control the center square - it's part of more potential winning combinations
2. Block your opponent's winning moves
3. Look for opportunities to create multiple winning paths
4. Pay attention to diagonal possibilities

## Troubleshooting
**Game doesn't start:**
- Ensure Python 3.12+ is installed
- Check if PyGame is properly installed
- Verify all game files are present

**Can't make a move:**
- Ensure it's your turn
- Click only on empty cells
- The game must be in active state (not game over)

**Game seems frozen:**
- Press R to restart the game
- If unresponsive, press Q and restart the application

## Need Help?
If you encounter any issues not covered in this guide, please:
1. Check the project's GitHub Issues page
2. Create a new issue with detailed problem description
3. Include your system information and error messages if any
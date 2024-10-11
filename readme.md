# Snake Game

## Description
A simple Snake game built using the `Pygame` library. In this game, the player controls a snake that grows in length as it consumes food. The game ends when the snake collides with the walls of the screen or itself. The objective is to survive as long as possible and achieve the highest score.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/JordanVF/snake-game.git
2. Navigate to the project directory: 
```bash
cd snake-game
```
3. Install the required dependencies:
```bash
pip install pygame
```
 
## Usage
1. Run the game
2. Control the snake using the arrow keys:
   - Left Arrow: Move left
   - Right Arrow: Move right
   - Up Arrow: Move up
   - Down Arrow: Move down
3. The game ends when the snake collides with the walls or its own body.
4. The score, which represents how many fruits the snake has eaten, is displayed at the top left corner of the screen.

## How it works
- Snake Movement: The snake moves based on the arrow keys pressed by the player. Its position updates in increments of 10 pixels in the specified direction.
- Food Generation: The food appears randomly on the screen. When the snake "eats" the food, it grows in length, and the score increases.
- Collision Detection: The game checks if the snake collides with the walls or itself, in which case the game ends.
- Score Display: The score is updated and displayed continuously as the snake consumes food.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


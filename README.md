# SnakeGame-Python

## Installation
* Clone the repository
```bash
git clone https://github.com/mehedi-shafi/SnakeGame-Python.git
```
* Install required dependencies from inside the directory
```bash
cd SnakeGame-Python
pip install -r requirements.txt
```

## Run the game
```bash
python game.py
```

## Changing here and there
You can change the game components and their actions very easily by changing and updating in necessary component. For example if you want to spawn some food with more than 1 score. You just have to update in 3 places.
1. 1st change the food class to accept a score as initializing paramete `def __init__(self, x, y, score):`
2. Change the score update from `score += 1` to `score += food.score`
3. Food spawing now should be using `self.food = Food(x, y, desired_score)`
That's all there to do for the simple task.

## Do update
Do share your creativity by forking and updating the code. Pull requests are always welcome. 
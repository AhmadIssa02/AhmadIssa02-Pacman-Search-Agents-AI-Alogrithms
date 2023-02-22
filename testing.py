from game import Actions
from game import Directions
dx, dy = Actions.directionToVector(Directions.SOUTH)
print(dx, dy)
walls = gameState.getWalls()
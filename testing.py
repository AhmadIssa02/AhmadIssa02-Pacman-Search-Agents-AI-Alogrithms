from game import Actions
from game import Directions
import search
import pacman
dx, dy = Actions.directionToVector(Directions.SOUTH)
print(dx, dy)
walls = gameState.getWalls()
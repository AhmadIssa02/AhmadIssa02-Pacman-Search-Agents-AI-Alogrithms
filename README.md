# Pacman-Search-Agents-Artificial-Intelligence-Alogrithms

This repository contains AI algorithms for search agents in the classic video game, Pacman. The algorithms implement different search techniques to help the Pacman agent find its way through various mazes.


# Getting Started

These instructions will help you get a copy of the project up and running on your local machine for testing and development purposes.

# Prerequisites:

Python 3.7 or later

Pygame

# Installation

Clone the repository to your local machine using the following command:

git clone https://github.com/username/pacman-search-agents.git

Navigate to the project directory:

cd pacman-search-agents

Install the required dependencies using the following command:

pip install -r requirements.txt

# Usage

To run the game and test the AI algorithms, run the following command:

python pacman.py

This will start the game with a default search agent. To use a different search algorithm, use the following command:

python pacman.py -l <layout> -p <agent> -a <algorithm>

  Replace <layout> with the name of the game layout you want to use, <agent> with the name of the search agent, and <algorithm> with the name of the search algorithm. For example:


python pacman.py -l mediumClassic -p SearchAgent -a astar
  
# Algorithms
The following search algorithms are implemented in this repository:

Depth-First Search (DFS)
Breadth-First Search (BFS)
Uniform-Cost Search (UCS)
A* Search (Astar)
Each algorithm is implemented as a separate Python class that inherits from the SearchAgent class.

# 🤖 AI Search Algorithm Solver

This project implements and visualizes three fundamental AI search algorithms—**Depth-First Search (DFS)**, **Breadth-First Search (BFS)**, and **A-Star (A\*) Search**—to solve a grid-based box-pushing puzzle, similar to Sokoban. The solution includes a visualizer built with Pygame to display the final path.

-----

## 🧩 The Problem: Box-Pushing Puzzle

The objective of this puzzle is to navigate a player on a 2D grid to push all the boxes onto their designated goal squares. The grid contains walls, empty floor spaces, a player, boxes, and goals.

### **Board Elements**

  * **`0` - Wall**: An impassable square. The player and boxes cannot move into a wall.
  * **`1` - Empty Floor**: A space the player can freely move into.
  * **`2` - Player**: The character you control. There is only one player on the board.
  * **`3` - Box**: An object that can be pushed by the player.
  * **`4` - Goal**: A target square where a box must be placed.

### **Rules**

1.  The player can move one step at a time **up, down, left, or right** into an empty floor square (`1`) or an empty goal square (`4`).
2.  The player can **push one box** at a time. This is done by moving onto a square occupied by a box, provided that the next square in the same direction is empty or a goal.
3.  The player **cannot push more than one box** at a time (i.e., you cannot push two boxes stacked together).
4.  The puzzle is solved when **every box is on a goal square**. The final position of the player does not matter.

For a detailed, formal description of the problem, please see [the assignment PDF](https://drive.google.com/file/d/1c2KwL1QsJ1robmZNQoKDUwFhYoxvy-pD/view?usp=sharing):

-----

## 🧠 Algorithms Implemented

This solver uses three different search strategies to find a solution to the puzzle.

### **Uninformed Search**

These algorithms search the state space without any prior knowledge of the distance to the goal.

  * **Breadth-First Search (BFS)**: An algorithm that explores the state space layer by layer. It guarantees finding the **shortest solution** in terms of the number of moves but can be slow and memory-intensive for large problems.
  * **Depth-First Search (DFS)**: This algorithm explores as deeply as possible along each branch before backtracking. It is very fast and memory-efficient but does not guarantee finding the shortest or optimal solution.

### **Informed Search**

This algorithm uses a "heuristic" function to intelligently guide the search toward the goal.

  * **A\* Search**: A powerful algorithm that combines the path cost (like BFS) with a heuristic estimate of the remaining distance to the goal. It is guaranteed to find the shortest path if the heuristic is admissible (never overestimates the true cost). This project implements two heuristics:
      * **Heuristic 1**: The Manhattan distance from the player to the nearest box.
      * **Heuristic 2**: The sum of the Manhattan distances from each box to its nearest goal.

-----

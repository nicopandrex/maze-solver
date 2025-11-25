# 🌀 Terminal Maze Generator & Solver (Python + curses)

This is a terminal-based **maze generator and pathfinding visualizer** built using Python’s `curses` library.  
It generates a random maze of any odd dimensions, then uses **Breadth-First Search (BFS)** to find the shortest path from the start (`O`) to the goal (`X`), animating the search in real time.

---

## ✨ Features

- Random maze generation using a DFS-based algorithm  
- BFS pathfinding with live animation  
- Color-coded display (walls, start, goal, and path)  
- Validated user input (must be odd numbers)  
- Option to generate multiple mazes in one session  

---

## ▶️ How to Run

```bash
python maze.py
```

You need the curses library if on Windows

```
pip install windows-curses
```

## Usage
Enter the maze length (odd number)

Enter the maze width (odd number)

Watch the solver animate the BFS search

Choose whether to generate another maze

If you get an error, resize your terminal window to full screen

If you want to speed up the animation lessen time.sleep(.05) in find_path:
```
 
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(.05)
        stdscr.refresh()
``

## Program Overview

The program:

Creates a grid filled with walls

Carves a maze using a randomized DFS algorithm

Places the start (O) at the top and the goal (X) at the bottom

Runs BFS to find the shortest path between them

Animates each BFS step in the terminal

Displays the final solved path using *

## Preview

<img width="528" height="588" alt="image" src="https://github.com/user-attachments/assets/e10b8aca-32c6-454b-9afd-5fbd62812849" />
<img width="1028" height="952" alt="image" src="https://github.com/user-attachments/assets/66601173-cebc-4ae0-9aac-d3bd71776428" />




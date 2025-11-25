import curses
from curses import wrapper
import queue
import time
import random



def maze_generator(length, width):
    maze = []
    
    while len(maze) < length:
        maze.append([])
    for i, col in enumerate(maze):
        while len(col) < width:
            maze[i].append("#")
    
    start_col = random.randrange(1, width, 2)
    end_col = random.randrange(1, width, 2)
    start_pos = (0, start_col)
    end_pos = (length - 1, end_col)
    maze[start_pos[0]][start_pos[1]] = " "
    maze[end_pos[0]][end_pos[1]] = " " 
    
    first = (1,start_col)
    maze[1][start_col] = " "

    
    visited = set()
    visited.add(first)
    stack =[]
    neighbors = find_2_away(maze,first[0],first[1])
    for neighbor in neighbors:
        if neighbor not in visited:
            stack.append((first,neighbor))
    
    while stack:
        comefrom, goto = stack.pop()
        if goto in visited:
            continue
        
        
        wall_row = (comefrom[0]+goto[0]) // 2
        wall_col = (comefrom[1]+goto[1]) // 2
        
        maze[goto[0]][goto[1]] = " "
        maze[wall_row][wall_col] = " "
        visited.add(goto)
        
        next_neighbors = find_2_away(maze,goto[0],goto[1])
        for next_neighbor in next_neighbors:
            if next_neighbor not in visited:
                stack.append((goto,next_neighbor))
    
    maze[start_pos[0]][start_pos[1]] = "O"
    maze[end_pos[0]][end_pos[1]] = "X"
    return maze
        
        
        
        
    
   
        
        

    
    
    
    
    


def print_maze(maze,stdscr,path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)
    green = curses.color_pair(3)
    
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"*",red)
            elif value == "X":
                stdscr.addstr(i,j*2,value,green)
            else:
                stdscr.addstr(i,j*2,value,blue)


def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j
            
    return None




def find_path(maze,stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze,start)
    q = queue.Queue()
    q.put((start_pos,[start_pos]))
    
    
    visited = set()
    visited.add(start_pos) 
    while not q.empty():
        current_pos, path = q.get()
        row,col = current_pos
        
        
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(.05)
        stdscr.refresh()
        
        
        if maze[row][col] == end:
            return path
        neighbors = find_neighbors(maze,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r,c = neighbor
            if maze[r][c] == "#":
                continue
        
            new_path = path + [neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)
        
def find_neighbors(maze,row,col):
    neighbors = []
    
    if row > 0: #UP 
        neighbors.append((row-1, col))
    if row + 1 < len(maze): #DOWN checks that the neighbor would be less than the height of maze
        neighbors.append((row+1,col))
    if col> 0: #LEFT checks
        neighbors.append((row,col-1))
    if col + 1 <len(maze[0]): #RIGHT : checks that the neighbor would be less than the width of the maze
        neighbors.append((row,col+1))
        
    return neighbors
    
def find_2_away(maze,row,col):
    neighbors = []

    if row - 2 >= 0 and maze[row - 2][col] == "#":  # UP
        neighbors.append((row - 2, col))
    if row + 2 < len(maze) and maze[row + 2][col] == "#":  # DOWN
        neighbors.append((row + 2, col))
    if col - 2 >= 0 and maze[row][col - 2] == "#":  # LEFT
        neighbors.append((row, col - 2))
    if col + 2 < len(maze[0]) and maze[row][col + 2] == "#":  # RIGHT
        neighbors.append((row, col + 2))

    random.shuffle(neighbors)  
    return neighbors
    
    
    
def get_validated_int(stdscr, prompt, y):
    while True:
        curses.echo()
        stdscr.move(y, 0)
        stdscr.clrtoeol()              
        stdscr.addstr(y, 0, prompt)

        stdscr.refresh()

        
        s = stdscr.getstr(y, len(prompt)).decode("utf-8")
        curses.noecho()

        
        try:
            n = int(s)
            if n % 2 == 1 and  0 < n <= 37:
                return n   
        except ValueError:
            pass

        
        stdscr.move(y + 1, 0)
        stdscr.clrtoeol()
        stdscr.addstr(y + 1, 0, "Invalid—must be an odd number between 1 and 37. Try again.")
        stdscr.refresh()

def prompt_yes_no(stdscr, y):
    curses.echo()
    stdscr.move(y, 0)
    stdscr.clrtoeol()
    stdscr.addstr(y, 0, "Generate another maze? (y/n): ")
    stdscr.refresh()

    choice = stdscr.getstr(y, len("Generate another maze? (y/n): ")).decode().lower()
    curses.noecho()

    return choice.startswith("y")


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        stdscr.clear()

        length = get_validated_int(stdscr, "Enter maze length (odd number between 1 and 37): ", 0)
        width = get_validated_int(stdscr, "Enter maze width  (odd number between 1 and 37): ", 1)

        maze = maze_generator(length, width)
        find_path(maze, stdscr)

        stdscr.addstr(3, 0, "")  
        stdscr.refresh()

        if not prompt_yes_no(stdscr, length + 3):
            break

    
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()

    
    

    
    
  
    
wrapper(main)



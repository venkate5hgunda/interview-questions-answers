import random

# Grid game

# Part 1: init the board
# n: board dimension, (nxn) square board
# row: position of player in Y dimension
# col: position of player in X dimension
# orientation: direction player is facing (N, E, S, W)

# Part 2: print method
# - v - 
# - - -
# - - -

# - is an empty space
# ^ is player facing north
# > is player facing east
# v is player facing south
# < is player facing west

# Part 3: move method
# move("FFLFR")

# F: step forward 1 grid position in whatever direction player is facing
# L: rotation 90 degrees in place to the left (counterclockwise)
# R: rotation 90 degrees in place to the right (clockwise)

# Part 4: wrap around
# start
# - - - 
# < - -
# - - -

# move(“F”)

# end
# - - - 
# - - <
# - - -

# Part 5: add enemies
# Add nEnemies randomly to the board
# They shouldn't overlap with the player, or each other.
# Print them as "E"

# Part 6: game over
# start
# - v - 
# - E -
# E - -

# move(“FF”)

# GAME OVER
# - - - 
# - X -
# E - -

# Part 7: [TIME OVER HERE !!!]
# start
# - v - 
# - - -
# E - -

# move(“FF”)

# end
# TOTAL POINTS: 2
# - . - 
# - . -
# E v -



b_size = 0
p_row, p_col = 0,0
orientations = ['N', 'E', 'S', 'W']
p_orient = 0
enemy_pos = []
game_over = False
score = 0
p_pos = []

def get_rand_pos():
    global p_row, p_col, enemy_pos
    pos = (random.randrange(0,b_size), random.randrange(0,b_size))
    flag=True # TRUE is valid
    if (p_row, p_col)==pos:
        flag=False
    for i in range(len(enemy_pos)):
        if pos==enemy_pos[i]:
            flag=False
    if not flag:
        pos = get_rand_pos()
    return pos

def init_game(n, row, col, orient, num_enemies):
    global b_size, p_row, p_col, p_orient, enemy_pos
    b_size, p_row, p_col = n, row, col
    p_orient = orientations.index(orient)
    enemy_pos = []
    for i in range(num_enemies):
        enemy_pos.append(get_rand_pos())

def print_state():
    global b_size, p_row, p_col, p_orient, enemy_pos, game_over
    orient_mappings = ['^', '>', 'v', '<']
    for i in range(b_size):
        curr_row = ''
        for j in range(b_size):
            if i==p_row and j==p_col:
                if game_over:
                    curr_row += 'X '
                else:
                    curr_row += orient_mappings[p_orient] + ' '
            elif (i, j) in enemy_pos:
                curr_row += 'E '
            else:
                curr_row += '- '
        print(curr_row)
        curr_row = ''

def move(moves):
    global b_size, p_row, p_col, p_orient, orientations, game_over, score, p_pos
    dir_moves = [[-1,0],[0,1],[1,0],[0,-1]]
    for move in moves:
        if move=='F':
            p_row, p_col = (p_row+dir_moves[p_orient][0])%b_size,(p_col+dir_moves[p_orient][1])%b_size
            score+=1
            p_pos.append((p_row, p_col))
        elif move=='L':
            p_orient = (p_orient-1)%len(orientations)
        else:
            p_orient = (p_orient+1)%len(orientations)
        if (p_row,p_col) in enemy_pos:
            game_over = True
            print('GAME OVER')
            print_state()
            break
        
def main():
    init_game(5, 1, 0, 'W', 10)
    print(b_size, p_row, p_col, orientations[p_orient], enemy_pos)
    # print_state()
    # init_game(5, 3, 2, 'E')
    # print_state()
    move("FFFF")
    # print_state()

main()
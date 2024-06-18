import random
import curses
#part 1
def setup_screen(screen):
    sh, sw = screen.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    curses.curs_set(0)
    win.timeout(100)
    #def the color pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Obstacles with inverted colors
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal and special food
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Snake in gray

    return win, sh, sw
#part 2
# Part of the game where we handle snake initialization and movement
def init_snake(win, sh, sw):
    # Initialize the snake starting in the middle of the window and moving right
    snake = [[sh//2, sw//2 + i] for i in range(3)]
    for y, x in snake:
        win.addch(y, x, 'O', curses.color_pair(3))  # Using the gray color for the snake
    return snake
#control the snake with the keybord
def move_snake(win, snake, key, sh, sw):
    # Determine the new head of the snake based on the last key pressed
    head = snake[0]
    if key == curses.KEY_DOWN:
        new_head = [head[0] + 1, head[1]]
    elif key == curses.KEY_UP:
        new_head = [head[0] - 1, head[1]]
    elif key == curses.KEY_LEFT:
        new_head = [head[0], head[1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [head[0], head[1] + 1]
    else:
        new_head = [head[0], head[1] + 1]  # Default move right if no key pressed

    # Screen wrapping
    new_head[0] = new_head[0] % sh
    new_head[1] = new_head[1] % sw

    # Insert the new head of the snake
    snake.insert(0, new_head)
    win.addch(new_head[0], new_head[1], 'O', curses.color_pair(3))

    return snake

#part 3
def create_food(win, snake, obstacles, sh, sw, special=False):
    while True:
        food = None
        if special:
            food = [random.randint(1, sh-1), random.randint(1, sw-1), 'X']
        else:
            food = [random.randint(1, sh-1), random.randint(1, sw-1), '\u03C0'] #this is the notation of y
        if food not in snake and food[:2] not in obstacles:
            win.addch(food[0], food[1], food[2])
            break
    return food

#part 4 eatting food and score, left for the paly_game function



#part 5
def create_obstacles(win, sh, sw):
    obstacles = []

    total_blocks = int(sh * sw * 0.05)  # Total blocks dedicated to obstacles
    max_possible_obstacles = total_blocks // 5  # Maximum number of obstacles if each is only 5 cells

    num_obstacles = random.randint(1, max_possible_obstacles)  # Randomly decide the number of obstacles
    used_blocks = 0

    while used_blocks < total_blocks and num_obstacles > 0:
        length = random.randint(5, total_blocks - used_blocks)  # Ensure the obstacle length does not exceed remaining blocks
        vertical = random.choice([True, False])  # Decide the orientation of the obstacle
        if vertical:
            start_x = random.randint(1, sh - length)  # Ensure obstacle fits within screen vertically
            start_y = random.randint(1, sw - 1)
        else:
            start_x = random.randint(1, sh - 1)
            start_y = random.randint(1, sw - length)  # Ensure obstacle fits within screen horizontally

        for i in range(length):
            if vertical:
                obstacle = [start_x + i, start_y]
            else:
                obstacle = [start_x, start_y + i]
            obstacles.append(obstacle)
            win.addch(obstacle[0], obstacle[1], '#', curses.color_pair(2) | curses.A_REVERSE)

        used_blocks += length  # Update the count of used blocks
        num_obstacles -= 1  # Decrement the count of obstacles to create

    return obstacles

#play the game
def play_game(win):
    sh, sw = win.getmaxyx()
    snake = init_snake(win, sh, sw)
    obstacles = create_obstacles(win, sh, sw)
    special_food = False
    food = create_food(win, snake, obstacles, sh, sw, special_food)
    score_normal = 0
    score_special = 0
    key = curses.KEY_RIGHT
    pause = False

    while True:
        next_key = win.getch()
        
        # Pause/Resume game
        if next_key == ord(' '):
            pause = not pause
            continue
        
        # Handle key presses
        if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            key = next_key
        
        # Continue on pause
        if pause:
            continue

        # Move the snake
        snake = move_snake(win, snake, key, sh, sw)

        # Check for collision with the boundaries or obstacles
        head = snake[0]
        if head in snake[1:] or head in obstacles:
            win.addstr(sh//2, sw//2, "Game Over!")
            win.addstr(sh//2 + 1, sw//2, f"Normal Food Eaten: {score_normal}, Special Food Eaten: {score_special}")
            win.refresh()
            win.getch()
            break

        # Check if snake eats food
        if head == food[:2]:
            if food[2] == 'X':
                score_special += 1
                special_food = True
            else:
                score_normal += 1
                special_food = False
            food = create_food(win, snake, obstacles, sh, sw, special_food)

            # Grow snake or shrink it based on special food
            if food[2] == 'X' and len(snake) > 1:
                tail = snake.pop()
                win.addch(tail[0], tail[1], ' ')
            else:
                win.addch(food[0], food[1], food[2])
        else:
            # Remove the snake's tail
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.refresh()

    # Allow time to read the game over message
    win.nodelay(False)
    win.getch()

# Main function to run the game
def main():
    curses.wrapper(play_game)

if __name__ == "__main__":
    main()

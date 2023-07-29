import pygame
import random
import sys
import json


#ini pygame
pygame.init()
def play_battleship():
    
    print("In this game: click on the grids to find the Battleship. After 20 tries, You lose :(")

    battleship_running = True
    while battleship_running:  
        # Set the dimensions of the game window
        window_width = 200
        window_height = 200
    
        # Set the colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)
    
        # Set the size of each cell on the game board
        cell_size = 40
    
        # Set the number of rows and columns on the game board
        board_size = 5
    
        # Set the number of turns the player has
        max_turns = 20
        
        # Set the location of the treasure
        ship_row = random.randint(0, board_size - 1)
        ship_col = random.randint(0, board_size - 1)
    
        # Create the game board
        board = []
        for _ in range(board_size):
            board.append([False] * board_size)
    
        # Create the window
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Battleship Game")
    
        # Game loop
        running = True
        turn = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
                if event.type == pygame.MOUSEBUTTONDOWN and turn < max_turns:
                    # Get the position of the mouse click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
    
                    # Calculate the row and column based on the mouse position
                    guess_row = mouse_y // cell_size
                    guess_col = mouse_x // cell_size
    
                    # Check if the guess is correct
                    if guess_row == ship_row and guess_col == ship_col:
                        print("Congratulations! You found the Battleship!")
                        running = False
                    else:
                        # Check if the guess is out of bounds
                        if (
                            guess_row < 0
                            or guess_row >= board_size
                            or guess_col < 0
                            or guess_col >= board_size
                        ):
                            print("Oops, that's not even in the ocean.")
                        # Check if the guess was already made
                        elif board[guess_row][guess_col]:
                            print("You guessed that one already.")
                        else:
                            print("You missed my Battleship!")
                            board[guess_row][guess_col] = True
    
                        turn += 1
                        if turn >= max_turns:
                            print("Game Over!")
  
            # Draw the game board
            for row in range(board_size):
                for col in range(board_size):
                    cell_color = white
                    if board[row][col]:
                        cell_color = blue
    
                    pygame.draw.rect(
                        window,
                        cell_color,
                        (col * cell_size, row * cell_size, cell_size, cell_size),
                    )
                    pygame.draw.rect(
                        window,
                        black,
                        (col * cell_size, row * cell_size, cell_size, cell_size),
                        1,
                    )
    
            pygame.quit
    
    # ... Code for the Battleship game ...




def play_scissors_paper_stone():
    print("Welcome to rock paper scissors!")

    choices = ["rock", "paper", "scissors"]
    while True:
      user_choice = input("Enter your choice (rock, paper, or scissors): ")
      if user_choice in choices:
        break
      else:
        print("Invalid Choice")
    bot_choice = choices[random.randint(0,2)]
    print("Player chose", user_choice)
    print("Bot chose", bot_choice)
    if user_choice == bot_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "paper" and bot_choice == "rock") or
        (user_choice == "scissors" and bot_choice == "paper")
    ):
         print("You win!")
    else:
        print("You lose!")

  
  
  
  
  
  
  
    # ... Code for the Scissors Paper Stone game ...

def play_tic_tac_toe():

  
  

  # Set up the game window
  WINDOW_SIZE = (300, 300)
  window = pygame.display.set_mode(WINDOW_SIZE)
  pygame.display.set_caption("Tic-Tac-Toe")

  # Define colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)

  # Define cell dimensions
  CELL_SIZE = 100

  # Define the board
  board = [[" " for _ in range(3)] for _ in range(3)]

  # Define the bot's symbol
  BOT_SYMBOL = "O"

  # Function to draw the tic-tac-toe board
  def draw_board():
    window.fill(WHITE)
    pygame.draw.line(window, BLACK, (CELL_SIZE, 0), (CELL_SIZE, WINDOW_SIZE[1]), 5)
    pygame.draw.line(window, BLACK, (CELL_SIZE * 2, 0), (CELL_SIZE * 2, WINDOW_SIZE[1]), 5)
    pygame.draw.line(window, BLACK, (0, CELL_SIZE), (WINDOW_SIZE[0], CELL_SIZE), 5)
    pygame.draw.line(window, BLACK, (0, CELL_SIZE * 2), (WINDOW_SIZE[0], CELL_SIZE * 2), 5)

    for row in range(3):
        for col in range(3):
            cell = board[row][col]
            if cell != " ":
                x = col * CELL_SIZE + CELL_SIZE // 2
                y = row * CELL_SIZE + CELL_SIZE // 2

                if cell == "X":
                    pygame.draw.line(window, BLACK, (x - 30, y - 30), (x + 30, y + 30), 5)
                    pygame.draw.line(window, BLACK, (x + 30, y - 30), (x - 30, y + 30), 5)
                else:
                    pygame.draw.circle(window, RED, (x, y), 30, 5)

    pygame.display.update()

  # Function to check if the game is over
  def check_game_over():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return True

    return False

  # Function for the bot's move
  def make_bot_move():
    # Try to win
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = BOT_SYMBOL
                if check_game_over():
                    return
                board[row][col] = " "

    # Try to block the player
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_game_over():
                    board[row][col] = BOT_SYMBOL
                    return
                board[row][col] = " "

    # Choose a random empty cell
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = BOT_SYMBOL
            return

  # Main game loop
  running = True
  player_turn = True  # True if it's the player's turn, False if it's the bot's turn

  while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn and not check_game_over():
            x, y = pygame.mouse.get_pos()
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            if board[row][col] == " ":
                board[row][col] = "X"
                player_turn = False

    if not player_turn and not check_game_over():
        make_bot_move()
        player_turn = True

    draw_board()

    if check_game_over():
        pygame.time.wait(1000)  # Wait for 1 second before resetting the board
        board = [[" " for _ in range(3)] for _ in range(3)]
        player_turn = True
  pygame.quit()


# ... Code for the Tic Tac Toe game ...

def play_platformer():


  
  print("Welcome to Platformer! \n In this game u use spacebar to jump and arrowkeys to move. \n Have Fun!")
  

  SCREEN_WIDTH = 1000
  SCREEN_HEIGHT = 600
  current_level = 0
  
  
  initiating_window = pygame.image.load("ballstor.png")
  initiating_window = pygame.transform.scale(initiating_window, (SCREEN_WIDTH, SCREEN_HEIGHT + 100))
  
  
  def game_initiating_window(screen):
      screen.blit(initiating_window, (0, 0))
      pygame.display.update()
      pygame.time.wait(3000)
      screen.fill(WHITE)
  
  
  SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Platformer")
  
  
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  
  
  class Player(pygame.sprite.Sprite):
      def __init__(self):
          super().__init__()
          self.surf = pygame.Rect((0, 0), (50, 50))
          self.image = pygame.image.load('amogus.png')
          self.image = pygame.transform.scale(self.image, self.surf.size)
          self.rect = self.image.get_rect()
          self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
          self.velocity = pygame.math.Vector2(0, 0)
          self.gravity = 0.5
          self.on_ground = False
          
      def death(self):
          self.kill()
             
  
      def update(self, platforms):
          self.velocity.y += self.gravity
          self.rect.move_ip(self.velocity.x, self.velocity.y)
  
          # Keep the player within the screen boundaries
          if self.rect.left < 0:
              self.rect.left = 0
          if self.rect.right > SCREEN_WIDTH:
              self.rect.right = SCREEN_WIDTH
          if self.rect.top < 0:
              self.rect.top = 0
  
          self.on_ground = False
          for platform in platforms:
              if self.rect.colliderect(platform.rect):
                  if self.velocity.y > 0:
                      self.rect.bottom = platform.rect.top
                      self.velocity.y = 0
                      self.on_ground = True
                  elif self.velocity.y < 0:
                      self.rect.top = platform.rect.bottom
                      self.velocity.y = 0
  
      def jump(self):
          if self.on_ground:
              self.velocity.y = -12
              self.on_ground = False
  
  
  class Platform(pygame.sprite.Sprite):
      def __init__(self, x, y):
          super().__init__()
          self.image = pygame.Surface((50, 50))
          self.image.fill(WHITE)
          image = pygame.transform.scale(pygame.image.load('block.png'), (50, 50))
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.topleft = (x, y)
  
  
  
  class Goal(pygame.sprite.Sprite):
      def __init__(self, x, y):
          super().__init__()
          self.image = pygame.Surface((50, 50))
          self.image.fill(WHITE)
          image = pygame.transform.scale(pygame.image.load('goal.png'), (50, 50))
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.topleft = (x, y)
  class Obstacle(pygame.sprite.Sprite):
      def __init__(self, x, y):
          super().__init__()
          self.image = pygame.Surface((50, 50))
          self.image.fill(WHITE)
          image = pygame.transform.scale(pygame.image.load('bomb.png'), (50, 50))
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.topleft = (x, y)
  
  levels = [
      "level1.json",
      "level2.json",
      "level3.json",
      "level4.json",
      "level5.json",
      "level6.json",
      "level7.json",
      "level8.json",
      "level9.json",
      'level10.json'
  ]
  
  
  
  
  def load_platforms_from_json(json_file):
      platforms = []
      with open(json_file, 'r') as file:
          data = json.load(file)
          for platform_data in data['platforms']:
              x = platform_data['x']
              y = platform_data['y']
              platform = Platform(x, y)
              platforms.append(platform)
      return platforms
  def load_goal_from_json(json_file):
    with open(json_file) as file:
      data=json.load(file)
    goal = Goal(data["goal"][0],data["goal"][1])
    return goal
  def load_obstacle_from_json(json_file):
      obstacles = []
      with open(json_file, 'r') as file:
          data = json.load(file)
          for obstacle_data in data["obstacle"]:
              x = obstacle_data['x']
              y = obstacle_data['y']
              obstacle = Obstacle(x, y)
              obstacles.append(obstacle)
      return obstacles
  def main():
      nonlocal current_level
      SCREEN.fill(BLACK)
      game_initiating_window(SCREEN)
      player = Player()
      player.rect.center = (0,20)
      platform_group = pygame.sprite.Group()
      goal_group = pygame.sprite.Group()
      obstacle_group=pygame.sprite.Group()
      all_sprites = pygame.sprite.Group()
      all_sprites.add(player)
      playerrect=player.rect
      platforms_data = load_platforms_from_json(levels[current_level])
      for platform in platforms_data:
          platform_group.add(platform)
          all_sprites.add(platform)
      obstacle_data = load_obstacle_from_json(levels[current_level])
      for obstacle in obstacle_data:
          obstacle_group.add(obstacle)
          all_sprites.add(obstacle)
      
      goal_data = load_goal_from_json(levels[current_level])
      goal_group.add(goal_data)
      all_sprites.add(goal_data)
      goalrect=goal_data.rect
      clock = pygame.time.Clock()
  
      while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
  
          keys = pygame.key.get_pressed()
  
          if keys[pygame.K_LEFT]:
              player.velocity.x = -5
          elif keys[pygame.K_RIGHT]:
              player.velocity.x = 5
          else:
              player.velocity.x = 0
  
          if keys[pygame.K_SPACE]:
              player.jump()
  
          player.update(platform_group)
  
          SCREEN.fill(BLACK)
          all_sprites.draw(SCREEN)
          if player.rect.bottom>= SCREEN_HEIGHT:
            player.rect.center = (0,20)
          if pygame.sprite.spritecollideany(player,obstacle_group):
            player.rect.center = (0,20)
          if pygame.Rect.colliderect(playerrect,goalrect):
            # Increment the level and reset the player's position
              current_level += 1
            
              if current_level >= len(levels):
                  print("Congratulations! You Win!")
                  # If the player has completed all levels, exit the game
                  pygame.quit()
                  sys.exit()
              else:
                  # Load the next level's platforms from the corresponding JSON file
                  platform_group.empty()
                  all_sprites.empty()
                  goal_group.empty()
                  obstacle_group.empty()
                  player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                  platforms_data = load_platforms_from_json(levels[current_level])
                  obstacle_data=load_obstacle_from_json(levels[current_level])
                  goal_data=load_goal_from_json(levels[current_level])
                  player.rect.center = (0,20)
                  for platform in platforms_data:
                      platform_group.add(platform)
                      all_sprites.add(platform)
                      all_sprites.add(player)
                  
                  goal_group.add(goal_data)
                  all_sprites.add(goal_data)
                  for obstacle in obstacle_data:
                    obstacle_group.add(obstacle)
                    all_sprites.add(obstacle)
                  goalrect=goal_data.rect
          # Display current level at the top right of the screen
          font = pygame.font.Font(None, 36)
          level_text = font.render(f"Level: {current_level + 1}", True, WHITE)
          SCREEN.blit(level_text, (SCREEN_WIDTH - 150, 20))
  
          pygame.display.flip()
          clock.tick(60)
  
          # Check if the player has completed the current level
          
  
  if __name__ == "__main__":
      main()
  
  


def start_game():
    endgame = False
    while not endgame:
        n = input("Choose game to play: \n 1. Battleship \n 2. Scissors Paper Stone \n 3. tic tac toe \n 4. Platformer \n 5. Exit \n")
  
        
        if n == "1":
            play_battleship()
        elif n == "2":
            play_scissors_paper_stone()
        elif n == "3":
            play_tic_tac_toe()
        elif n == "4":
            play_platformer()
        elif n == "5":
            endgame = True
            print("Thank you for Playing!")
        else:
            print("Invalid input. Please choose a valid game option (1, 2, 3, 4, or 5).")


if __name__ == "__main__":
    start_game()

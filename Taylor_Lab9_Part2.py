import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()

# ========================================
# CONSTANTS - Define once, use everywhere
# ========================================

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (RGB format: Red, Green, Blue)
# New color palette: Purple, Blue, Teal, and Pink
DARK_PURPLE = (62, 31, 71)       # Background color (deep purple)
PURPLE = (125, 60, 152)          # Medium purple
LIGHT_PURPLE = (180, 120, 200)   # Light purple
TEAL = (0, 200, 180)             # Bright teal
BLUE = (80, 150, 230)            # Sky blue
PINK = (255, 105, 180)           # Hot pink
LIGHT_PINK = (255, 182, 193)     # Light pink
WHITE = (255, 255, 255)          # White for contrast
LIGHT_TEAL = (100, 255, 220)     # Light teal

# Frame rate
FPS = 60

# Game settings
WORD_FALL_SPEED = 1.5      # Constant fall speed (doesn't change anymore)
BOTTOM_LIMIT = 580         # If word reaches this Y position, player loses
TARGET_SCORE = 100         # Score needed to win
WORDS_PER_LEVEL = 10       # Every 10 correct answers, add one more word

# Backspace settings
BACKSPACE_DELAY = 500      # Milliseconds before held backspace starts repeating
BACKSPACE_INTERVAL = 50    # Milliseconds between each deletion when holding

# Milestone scores where we show motivational break screens
BREAK_MILESTONES = [20, 40, 60, 80]

# Game states - different phases the game can be in
STATE_START = "start"          # Start screen with instructions
STATE_PLAYING = "playing"      # Active gameplay
STATE_BREAK = "break"          # Motivational break screen
STATE_GAME_OVER = "game_over"  # Game ended (win or lose)

# List of words the player might need to type
WORD_LIST = ["cat", "dog", "bird", "fish", "frog", "bear", "lion", "wolf", 
             "tree", "sun", "moon", "star", "rain", "wind", "fire", "rock"]

# ========================================
# GAME SETUP - Initialize game components
# ========================================

# Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Type Blast")

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Set up fonts for text
game_font = pygame.font.Font(None, 48)        # Font for the falling word
input_font = pygame.font.Font(None, 36)       # Font for what player types
game_over_font = pygame.font.Font(None, 72)   # Big font for GAME OVER
score_font = pygame.font.Font(None, 36)       # Font for score display
win_font = pygame.font.Font(None, 72)         # Big font for YOU WIN
title_font = pygame.font.Font(None, 64)       # Font for title on start screen
instruction_font = pygame.font.Font(None, 32) # Font for instructions
message_font = pygame.font.Font(None, 56)     # Font for motivational messages

# ========================================
# GAME VARIABLES - Store game state
# ========================================

# Position of the falling word
word_x = 350  # Horizontal position
word_y = 20   # Vertical position

# What the player has typed so far
player_input = ""  # Starts as empty string

# Game state - what phase of the game we're in
game_state = STATE_START  # Start at the start screen

# Game variables
player_won = False      # Tracks if the player won (True) or lost (False)
score = 0               # Player's score, starts at zero
num_words = 1           # How many words to show (starts at 1, increases every 10 correct)
target_phrase = ""      # The phrase the player needs to type

# Pause state
paused = False  # Tracks if the game is paused (manual pause with P key)

# Backspace hold tracking
backspace_held = False           # Is backspace currently being held down?
backspace_timer = 0              # Timer for controlling deletion rate
backspace_initial_delay = True   # Are we in the initial delay before repeating?

# ========================================
# GAME FUNCTIONS - Helper functions
# ========================================

def draw_centered_text(text, y_position, color, font):
    """
    Render text, center it horizontally, and draw it on screen.
    
    Parameters:
    text - the string to display
    y_position - vertical position (Y coordinate)
    color - RGB color tuple
    font - pygame font object
    """
    # Step 1: Render the text into a surface
    text_surface = font.render(text, True, color)
    
    # Step 2: Get the width of the rendered text
    text_width = text_surface.get_width()
    
    # Step 3: Calculate the X position to center it
    text_x = (SCREEN_WIDTH - text_width) // 2
    
    # Step 4: Draw it on the screen
    screen.blit(text_surface, (text_x, y_position))


def draw_text_lines(lines, start_y, colors, font):
    """
    Draw multiple lines of text, each centered horizontally.
    
    Parameters:
    lines - list of strings to display
    start_y - starting Y position for first line
    colors - list of colors (or single color for all lines)
    font - pygame font object
    
    Returns:
    The Y position after the last line (useful for positioning more content below)
    """
    y_position = start_y
    
    # If colors is a single color, use it for all lines
    if not isinstance(colors, list):
        colors = [colors] * len(lines)
    
    # Draw each line
    for i, line in enumerate(lines):
        color = colors[i] if i < len(colors) else WHITE
        draw_centered_text(line, y_position, color, font)
        y_position += 40  # Move down for next line
    
    return y_position


def generate_target_phrase(num_words):
    """
    Generate a phrase with the specified number of words.
    
    Parameters:
    num_words - how many words to include in the phrase
    
    Returns:
    A string with num_words random words separated by spaces
    """
    # Pick num_words random words from the list
    words = [random.choice(WORD_LIST) for _ in range(num_words)]
    
    # Join them with spaces
    # Example: ["cat", "dog", "fish"] becomes "cat dog fish"
    return " ".join(words)


def reset_word_position():
    """
    Reset the falling word to the top of the screen.
    This is called when the player successfully types a phrase.
    """
    global word_y
    word_y = 20


def handle_correct_answer():
    """
    Handle all the logic when the player types the correct phrase.
    Updates score, checks for milestones, generates new phrase, etc.
    """
    global score, num_words, game_state, target_phrase, player_input, player_won
    
    # Add 1 point to the score
    score += 1
    
    # Check if we hit a milestone that triggers a break screen
    if score in BREAK_MILESTONES:
        # Show the motivational break screen!
        game_state = STATE_BREAK
    
    # Check if we should increase the number of words
    # Every 10 correct answers, add one more word
    num_words = (score // WORDS_PER_LEVEL) + 1
    
    # Check if player reached the target score (WIN CONDITION!)
    if score >= TARGET_SCORE:
        # Player wins!
        game_state = STATE_GAME_OVER  # Change to game over state
        player_won = True  # Player won!
    else:
        # Haven't won yet, keep playing (unless we're on a break screen)
        
        if game_state != STATE_BREAK:
            # Generate a new phrase with the current number of words
            target_phrase = generate_target_phrase(num_words)
            
            # Reset the word to the top of the screen
            reset_word_position()
            
            # Clear the player's input so they can type again
            player_input = ""


def handle_backspace_held(delta_time):
    """
    Handle continuous backspace deletion when the key is held down.
    
    Parameters:
    delta_time - milliseconds since last frame
    """
    global backspace_timer, backspace_initial_delay, player_input
    
    # Increment the timer
    backspace_timer += delta_time
    
    # Check if we're still in the initial delay
    if backspace_initial_delay:
        # Wait for the initial delay before starting to repeat
        if backspace_timer >= BACKSPACE_DELAY:
            # Initial delay is over, start repeating
            backspace_initial_delay = False
            backspace_timer = 0
            # Delete a character
            if player_input:
                player_input = player_input[:-1]
    else:
        # We're in repeat mode, delete at regular intervals
        if backspace_timer >= BACKSPACE_INTERVAL:
            # Time to delete another character
            if player_input:
                player_input = player_input[:-1]
            # Reset timer for next deletion
            backspace_timer = 0


def draw_start_screen():
    """
    Draw the start screen with title and instructions.
    """
    # Draw title in bright teal
    draw_centered_text("Type Blast", 100, TEAL, title_font)
    
    # Draw instructions in white and pink
    instructions = [
        "Press P to pause during the game.",
        "",
        "Press SPACE to start!"
    ]
    
    # Colors for each line (white for most, pink for last line)
    colors = [WHITE, WHITE, PINK]
    
    # Draw all instruction lines
    draw_text_lines(instructions, 190, colors, instruction_font)


def draw_break_screen():
    """
    Draw the motivational break screen.
    """
    # Draw score achieved in pink
    score_text = f"Score: {score} / {TARGET_SCORE}"
    draw_centered_text(score_text, 160, PINK, message_font)
    
    # Draw break prompt
    break_prompt = [
        "",
        "Take a breather if you need it!",
        "",
        "Press SPACE when you're ready to continue"
    ]
    
    # Colors for each line (white for most, light pink for last line)
    colors = [WHITE, WHITE, WHITE, LIGHT_PINK]
    
    # Draw all prompt lines
    draw_text_lines(break_prompt, 220, colors, instruction_font)


def draw_playing_screen():
    """
    Draw the main gameplay screen with falling phrase, player input, and score.
    """
    # Draw falling phrase in light teal
    phrase_surface = game_font.render(target_phrase, True, LIGHT_TEAL)
    # Center the phrase horizontally
    phrase_width = phrase_surface.get_width()
    phrase_x = (SCREEN_WIDTH - phrase_width) // 2
    screen.blit(phrase_surface, (phrase_x, word_y))
    
    # Draw what the player has typed in pink
    input_surface = input_font.render(player_input, True, PINK)
    screen.blit(input_surface, (350, 550))
    
    # Draw score in blue
    score_text = f"Score: {score} / {TARGET_SCORE}"
    score_surface = score_font.render(score_text, True, BLUE)
    screen.blit(score_surface, (10, 10))
    
    # If paused, show PAUSED message and instructions
    if paused:
        draw_centered_text("PAUSED", 250, PINK, game_over_font)
        draw_centered_text("Press P to continue", 350, WHITE, instruction_font)


def draw_game_over_screen():
    """
    Draw the game over screen (win or lose).
    """
    # Check if player won or lost
    if player_won:
        # Player won! Show victory message in light teal
        draw_centered_text("YOU WIN!", 250, LIGHT_TEAL, win_font)
    else:
        # Player lost! Show game over message in pink
        draw_centered_text("GAME OVER", 250, PINK, game_over_font)
    
    # Show final score in blue
    final_score_text = f"Final Score: {score}"
    draw_centered_text(final_score_text, 350, BLUE, score_font)


# Generate the first target phrase
target_phrase = generate_target_phrase(num_words)

# ========================================
# MAIN GAME LOOP
# ========================================

running = True
while running:
    
    # Get the time since last frame (in milliseconds)
    delta_time = clock.get_time()
    
    # ----------------------------------------
    # 1. EVENT HANDLING
    # ----------------------------------------
    # Process user inputs (keyboard, mouse, window events)
    
    for event in pygame.event.get():
        # Check if user wants to quit
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key presses (KEYDOWN = key just pressed)
        if event.type == pygame.KEYDOWN:
            
            # START SCREEN - Press SPACE to begin
            if game_state == STATE_START:
                if event.key == pygame.K_SPACE:
                    # Start the game!
                    game_state = STATE_PLAYING
            
            # BREAK SCREEN - Press SPACE to continue
            elif game_state == STATE_BREAK:
                if event.key == pygame.K_SPACE:
                    # Continue playing!
                    game_state = STATE_PLAYING
            
            # PLAYING - Handle gameplay keys
            elif game_state == STATE_PLAYING:
                # Press P to pause/unpause
                if event.key == pygame.K_p:
                    paused = not paused  # Toggle pause
                
                # Only process typing if not paused
                elif not paused:
                    # Check if the key was backspace
                    if event.key == pygame.K_BACKSPACE:
                        # Delete one character immediately
                        if player_input:
                            player_input = player_input[:-1]
                        
                        # Start the backspace hold tracking
                        backspace_held = True
                        backspace_timer = 0
                        backspace_initial_delay = True
                    else:
                        # Add the typed character to player_input
                        player_input += event.unicode
        
        # Handle key releases (KEYUP = key just released)
        elif event.type == pygame.KEYUP:
            # If backspace was released, stop the hold tracking
            if event.key == pygame.K_BACKSPACE:
                backspace_held = False
                backspace_timer = 0
                backspace_initial_delay = True
    
    
    # ----------------------------------------
    # Handle held backspace (continuous deletion)
    # ----------------------------------------
    if game_state == STATE_PLAYING and not paused and backspace_held:
        handle_backspace_held(delta_time)
    
    
    # ----------------------------------------
    # 2. GAME LOGIC
    # ----------------------------------------
    # Update game state (move objects, check collisions, update scores)
    
    # Only update game if we're playing AND not paused
    if game_state == STATE_PLAYING and not paused:
        # Make the word fall down (constant speed now)
        word_y += WORD_FALL_SPEED
        
        # Check if word reached the bottom of the screen
        if word_y >= BOTTOM_LIMIT:
            # Player loses! Word reached the bottom
            game_state = STATE_GAME_OVER  # Change to game over state
            player_won = False  # Player lost
        
        # Check if player typed the correct phrase
        if player_input == target_phrase:
            # Success! The player typed the correct phrase
            handle_correct_answer()
    
    
    # ----------------------------------------
    # 3. DRAWING
    # ----------------------------------------
    # Render everything to the screen
    
    # Clear the screen with background color (deep purple)
    screen.fill(DARK_PURPLE)
    
    # Draw different things depending on the game state
    
    # ===== START SCREEN =====
    if game_state == STATE_START:
        draw_start_screen()
    
    # ===== BREAK SCREEN =====
    elif game_state == STATE_BREAK:
        draw_break_screen()
    
    # ===== PLAYING =====
    elif game_state == STATE_PLAYING:
        draw_playing_screen()
    
    # ===== GAME OVER =====
    elif game_state == STATE_GAME_OVER:
        draw_game_over_screen()
    
    # Update the display to show everything we drew
    pygame.display.flip()
    
    
    # ----------------------------------------
    # 4. FRAME RATE
    # ----------------------------------------
    # Control how fast the game runs
    clock.tick(FPS)


# ========================================
# CLEANUP - End the game properly
# ========================================
pygame.quit()
sys.exit()
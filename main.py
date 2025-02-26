# Arden Boettcher
# 2/24/25
# Main

import pygame
import space
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Stars")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True



# Main loop
def main():
  # The bool for the main loop
  # ship = list(config.ship)
  running = True
  stars = space.Space((config.WIDTH, config.HEIGHT), 1000)

  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    # Star things
    stars.draw(screen)

    stars.movedown()

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()

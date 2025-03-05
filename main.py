# Arden Boettcher
# 2/24/25
# Main

import pygame

import game_class
import space
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Stars")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events(event):
  # Quits the game when you press the x
  if event.type == pygame.QUIT:
    return False
  return True



# Main loop
def main():
  # The bool for the main loop
  running = True
  stars = space.Space((config.WIDTH, config.HEIGHT), 10)
  game = game_class.Game()

  dt = 0

  while running:

    # Call events / update running
    for event in pygame.event.get():
      running = main_events(event)
      game.events(event)

    game.update(dt)

    # Fills window
    screen.fill(config.WHITE)

    # Star things
    stars.draw(screen)
    game.draw(screen)

    stars.movedown()

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    dt = clock.tick(config.FPS) / 1000

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()

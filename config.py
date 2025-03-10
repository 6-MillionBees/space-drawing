# Arden Boettcher
# 2/24/25
# Template Config

import pygame as pg

# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)


BLUE = (0, 0, 255)
LIGHT_BLUE = (120, 120, 255)



# Outline

def outline(rect, weight = 2):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  # pg.draw.rect(surface, color, outrect)
  return outrect

def rainbow(color: list[0]):
  red = color[0]
  green = color[1]
  blue = color[2]

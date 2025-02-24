# Arden Boettcher
# 2/24/25
# Space Background Class

import pygame as pg
import config
from random import randint

class Stars:
  def __init__(self, num_of_stars: int, size: tuple[int, int], speed) -> None:
    self.pos = (10, 10)
    self.stars: list[pg.Rect] = []
    for x in range(num_of_stars):
      rect_size = randint(2, 5)
      self.stars.append(pg.Rect((randint(0, size[0]), randint(0, size[1])),  (rect_size, rect_size)))


  def draw(self, surface):
    for rect in self.stars:
      rect.left += self.pos[0]
      rect.top += self.pos[1]
      pg.draw.rect(surface, config.WHITE, rect)
# Arden Boettcher
# 2/24/25
# Space Background Class

import pygame as pg
import config
from random import randint

class Stars:
  def __init__(self, num_of_stars: int, size: tuple[int, int], speed: int, star_size_multiplier) -> None:
    self.size = size
    self.speed = speed
    self.pos1 = [0, 0]
    self.stars: list[pg.Rect] = []
    for x in range(num_of_stars):
      rect_size = int(randint(2, 5) * star_size_multiplier)
      self.stars.append(pg.Rect((randint(0, size[0]), randint(0, size[1])),  (rect_size, rect_size)))

    self.pos2 = [0, self.size[1]]
    self.stars2: list[pg.Rect] = []
    for rect in self.stars:
      self.stars2.append(rect)


  def movedown(self):
    self.pos1[1] += self.speed
    self.pos2[1] += self.speed

    if self.pos1[1] > self.size[1]:
      self.pos1[1] -= self.size[1] * 2

    if self.pos2[1] > self.size[1]:
      self.pos2[1] -= self.size[1] * 2


  def draw(self, surface):
    for rect in self.stars:
      temp_rect = pg.Rect(rect)
      temp_rect.left += self.pos1[0]
      temp_rect.top += self.pos1[1]
      pg.draw.rect(surface, config.WHITE, temp_rect)
    for rect in self.stars2:
      temp_rect = pg.Rect(rect)
      temp_rect.left += self.pos2[0]
      temp_rect.top += self.pos2[1]
      pg.draw.rect(surface, config.WHITE, temp_rect)



class Space:
  def __init__(self, size: tuple[int, int], num_layers):
    self.background = pg.Surface(size)
    self.background.fill(config.BLACK)
    self.pos = (0, 0)
    self.layers = [Stars(randint(15, 20), size, x + 1, x/num_layers) for x in range(1, num_layers + 1, 1)]


  def draw(self, surface):
    surface.blit(self.background, self.pos)
    for layer in self.layers:
      layer.draw(surface)

  def movedown(self):
    for layer in self.layers:
      layer.movedown()
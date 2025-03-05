# Arden Boettcher
# 3/4/25
# Projectile Classes

import pygame as pg


class Projectile:
  def __init__(self,
      pos: list[int],
      color: tuple[int],
      speed: int,
      damage: int
    ):
    self.pos = pos
    self.color = color
    self.speed = speed
    self.damage = damage

    self.image = pg.Rect(0, 0, 2, 3)
    self.image.center = self.pos
    self.hitrect = self.image.copy()

  def update(self, dt):
    self.pos[1] += self.speed * dt
    self.image.center = self.pos
    self.hitrect = self.image
    print(dt)

  def draw(self, surface):
    pg.draw.rect(surface, self.color, self.image)
# Arden Boettcher
# 3/4/25
# Projectile Classes

import pygame as pg
import config as c

class Projectile(pg.sprite.Sprite):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int],
      color: tuple[int],
      speed: int,
      damage: int
    ):

    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.speed = speed
    self.damage = damage

    self.image = pg.Rect(0, 0, 4, 6)
    self.image.center = self.pos
    self.hitrect = self.image.copy()

  def update(self, dt):
    self.pos[1] += self.speed * dt
    self.image.center = self.pos
    self.hitrect = self.image.copy()
    self.check_pos()

  def check_pos(self):
    if (
      self.pos[0] < -50 or
      self.pos[0] > c.WIDTH + 50 or
      self.pos[1] < -50 or
      self.pos[1] > c.HEIGHT + 50
    ):
      self.kill()


  def draw(self, surface):
    pg.draw.rect(surface, self.color, self.image)
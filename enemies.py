# Arden Boettcher
# 3/4/25
# Enemy classes

import pygame as pg
import config as c
from projectiles import Projectile
from random import randint

class Enemy:
  def __init__(self,
      pos: list[int]
    ):
    self.alive = True
    self.pos = pos
    self.health = randint(10, 15)
    self.image = pg.Rect(pos, (10, 20))
    self.hitrect = self.image.copy()

  def draw(self, surface):
    pg.draw.rect(surface, c.RED, self.image)

  def update(self, dt):
    self.image = pg.Rect(self.pos, (10, 20))
    if self.health <= 0:
      self.alive = False

  def is_hit(self, proj) -> bool:
    if self.hitrect.colliderect(proj.hitrect):
      return True
    return False


  def hit(self, proj: Projectile):
    self.health -= proj.damage

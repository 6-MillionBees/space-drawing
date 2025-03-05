# Arden Boettcher
# 3/4/25
# Enemy classes

import pygame as pg
import config as c
from projectiles import Projectile
from random import randint

class Enemy(pg.sprite.Sprite):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int]
    ):
    super().__init__(groups)
    self.alive: bool = True
    self.pos = pos
    self.health = randint(10, 15)

    self.define_surface()

  def define_surface(self):
    self.image = pg.Surface((10, 20))
    pg.draw.rect(self.image, c.RED, pg.Rect((0, 0), (10, 20)))
    self.hitrect = self.image.get_rect()
    self.hitrect.topleft = self.pos

  def draw(self, surface):
    surface.blit(self.image, self.pos)

  def update(self, dt):
    self.hitrect = self.image.get_rect()
    self.hitrect.topleft = self.pos
    if self.health <= 0:
      self.alive = False

  def is_hit(self, proj) -> bool:
    if self.hitrect.colliderect(proj.hitrect):
      return True
    return False


  def hit(self, proj: Projectile):
    self.health -= proj.damage



class Pathed_Enemy(Enemy):
  def __init__(self, groups: pg.sprite.Group, pos: list[int], path: list[int]):
    super().__init__(groups, pos)
    self.path = path
    self.checkpoint = 0



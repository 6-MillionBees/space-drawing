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
    self.direction = pg.Vector2(1, 0).normalize()
    self.speed = 100

    self.define_surface()

  def define_surface(self):
    self.image = pg.Surface((20, 20))
    pg.draw.rect(self.image, c.RED, pg.Rect((0, 0), (20, 20)))
    self.hitrect = self.image.get_rect()
    self.hitrect.topleft = self.pos

  def draw(self, surface):
    surface.blit(self.image, self.pos)

  def update(self, dt):
    self.hitrect = self.image.get_rect()
    self.hitrect.topleft = self.pos
    if self.health <= 0:
      self.alive = False
    self.move(dt)
    self.check_pos()

  def is_hit(self, proj) -> bool:
    if self.hitrect.colliderect(proj.hitrect):
      return True
    return False

  def move(self, dt):
    self.pos += self.direction * self.speed * dt

  def check_pos(self):
    if self.hitrect.left <= 0:
      self.hitrect.left -= self.hitrect.left
      self.direction = self.direction.reflect(self.direction)

    if self.hitrect.right >= c.WIDTH:
      self.hitrect.right -= c.WIDTH - self.hitrect.right
      self.direction = self.direction.reflect(self.direction)



  def hit(self, proj: Projectile):
    self.health -= proj.damage



class Pathed_Enemy(Enemy):
  def __init__(self, groups: pg.sprite.Group, pos: list[int], path: list[int]):
    super().__init__(groups, pos)
    self.path = path
    self.checkpoint = 0

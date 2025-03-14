# Arden Boettcher
# 3/4/25
# Projectile Classes

import pygame as pg
from pygame.sprite import Group
import config as c

class Projectile(pg.sprite.Sprite):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int],
      color: tuple[int],
      speed: int,
      damage: int,
      size: tuple[int]
    ):

    super().__init__(groups)
    self.direction = pg.Vector2(0, -1).normalize()
    self.pos = pos
    self.color = color
    self.speed = speed
    self.damage = damage
    self.size = size
    self.create_surf()


  def create_surf(self):
    self.image = pg.Surface((4, 6))
    self.hitrect = self.image.get_rect(center = self.pos)
    self.image_rect = self.image.get_rect(center = self.pos)
    pg.draw.rect(self.image, self.color, pg.Rect(0, 0, 4, 6))

  def update(self, dt):
    self.pos += self.direction * self.speed * dt
    self.hitrect.center = self.pos
    self.color = c.rainbow(self.color, 10)
    self.create_surf()
    self.check_pos()

  def check_pos(self):
    if (
      self.pos[0] < -50 or
      self.pos[0] > c.WIDTH + 50 or
      self.pos[1] < -50 or
      self.pos[1] > c.HEIGHT + 50
    ):
      self.kill()

  def hit(self):
    pass


  def draw(self, surface):
    surface.blit(self.image, self.image_rect)



class Bomb_Proj(Projectile):
  def __init__(self, groups: Group, pos: list[int], color: tuple[int], speed: int, damage: int):
    super().__init__(groups, pos, color, speed, damage)
    self.falloff = 300

  def update(self, dt):
    super().update(dt)
    self.speed -= self.falloff * dt
    self.check_speed()

  # def check_speed(self):

  def hit(self):
    self.explode()

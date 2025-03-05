# Arden Boettcher
# 3/4/25
# Partciles

import pygame as pg
import config as c
from random import randint

class Particle(pg.sprite.Sprite):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int],
      color: tuple[int],
      direction: pg.math.Vector2,
      speed: float,
      slow: float
    ):
    super().__init__(groups)
    self.slow = slow
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed
    self.fade_speed = 0
    self.alpha = 255
    self.size = 4

    self.create_surf()

  def move(self, dt):
    self.pos += self.direction * self.speed * dt
    self.speed -= self.slow * dt
    self.rect.center = self.pos

  def fade(self, dt):
    self.alpha -= self.fade_speed * dt
    self.image.set_alpha(self.alpha)

  def check_pos(self):
    if (
      self.pos[0] < -50 or
      self.pos[0] > c.WIDTH + 50 or
      self.pos[1] < -50 or
      self.pos[1] > c.HEIGHT + 50
    ):
      self.kill()

  def check_alpha(self):
    if self.alpha <= 0:
      self.kill()

  def update(self, dt):
    self.move(dt)
    self.fade(dt)
    self.check_pos()
    self.check_alpha()


  def create_surf(self):
    self.image = pg.Surface((self.size, self.size)).convert_alpha()
    self.image.set_colorkey(c.BLACK)

    self.rect = self.image.get_rect()
    self.rect.center = self.pos

    pg.draw.rect(self.image, c.RED, self.rect)


  def draw(self, surface):
    surface.blit(self.image, self.pos)


class Explosion(Particle):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int],
      color: tuple[int],
      speed: int,
      max_size: int,
      weight: int
    ):
    direction = pg.Vector2(0, 0)
    super().__init__(groups, pos, color, direction, speed, 0)
    self.t0 = pg.time.get_ticks()
    self.max_size = max_size
    self.size = 2
    self.inflate_speed = 200
    self.weight = weight

  def check_size(self):
    if self.size > self.max_size:
      self.kill()

  def update(self, dt):
    self.move(dt)
    self.explode(dt)
    self.check_size()
    self.check_pos()

  def explode(self, dt):
    self.size += self.inflate_speed * dt

  def draw(self, surface):
    pg.draw.circle(surface, self.color, self.pos, self.size, self.weight)
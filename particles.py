# Arden Boettcher
# 3/4/25
# Partciles

import pygame as pg
from pygame.sprite import Group
import config as c
from random import randint

class Particle(pg.sprite.Sprite):
  def __init__(self,
      groups: pg.sprite.Group,
      pos: list[int],
      color: tuple[int],
      direction: pg.math.Vector2,
      speed: float
    ):
    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed
    self.fade_speed = 0
    self.alpha = 255
    self.size = 4

    self.create_surf()

  def move(self, dt: float):
    self.pos += self.direction * self.speed * dt
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

    pg.draw.rect(self.image, self.color, self.rect)


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
    super().__init__(groups, pos, color, direction, speed)
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



class Slowed_Part(Particle):
  def __init__(self, groups: Group, pos: list[int], color: tuple[int], direction: pg.Vector2, speed: float, slow: float):
    super().__init__(groups, pos, color, direction, speed)
    self.slow = slow
    self.timer = 0
    self.lifespan = 300

  def move(self, dt: float):
    self.pos += self.direction * self.speed * dt
    self.speed -= self.slow * dt

  def check_time(self):
    if self.timer + self.lifespan <= pg.time.get_ticks():
      self.kill()

  def check_speed(self):
    if self.speed <= 0:
      self.speed = 0
      self.slow = 0
      self.check_time()

  def update(self, dt):
    self.move(dt)
    self.fade(dt)
    self.check_pos()
    self.check_speed()
    self.check_alpha()



class Rainbow_Slowed_Part(Slowed_Part):
  def __init__(self,
      groups: Group,
      pos: list[int],
      color: tuple[int],
      direction: pg.Vector2,
      speed: float,
      slow: float
    ):
    super().__init__(groups, pos, color, direction, speed, slow)
    self.color = (255, 0, 0)

  def update(self, dt):
    self.move(dt)
    self.fade(dt)
    self.check_pos()
    self.check_speed()
    self.check_alpha()
    self.color = c.rainbow(self.color, 6)
    pg.draw.rect(self.image, self.color, self.rect)

  def create_surf(self):
    self.image = pg.Surface((self.size, self.size)).convert_alpha()
    self.image.set_colorkey(c.BLACK)

    self.rect = self.image.get_rect()

    pg.draw.rect(self.image, self.color, self.rect)
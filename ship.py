# Arden Boettcher
# 3/3/25
# Ship Class

import pygame as pg
import config as c


class Ship:
  def __init__(self):
    self.ship = pg.image.load("sprites/ship.png")
    self.ship.convert_alpha()
    self.pos = [100, 100]
    self.rect = self.ship.get_rect()
    self.hitrect = pg.Rect(0, 0, 25, 25)

    self.rect.center = self.pos
    self.hitrect.center = self.pos


  def draw(self, surface: pg.Surface):
    self.hitrect.center = self.pos
    self.rect.center = self.pos
    pg.draw.rect(surface, c.RED, self.hitrect, 2)
    surface.blit(self.ship, self.rect)


  def check_movement(self):
    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
      self.moveup()
    if keys[pg.K_DOWN]:
      self.movedown()
    if keys[pg.K_LEFT]:
      self.moveleft()
    if keys[pg.K_RIGHT]:
      self.moveright()

  def events(self, event):
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        self.fire()


  def fire(self):
    print("pew")


  def moveup(self):
    self.pos[1] -= 5
    self.hitrect.center = self.pos
    if self.hitrect.top < 0:
      self.pos[1] = 0 + (self.hitrect.height // 2)

  def movedown(self):
    self.pos[1] += 5
    self.hitrect.center = self.pos
    if self.hitrect.bottom > c.HEIGHT:
      self.pos[1] = c.HEIGHT - (self.hitrect.height // 2)

  def moveleft(self):
    self.pos[0] -= 8
    self.hitrect.center = self.pos
    if self.hitrect.left < 0:
      self.pos[0] = 0 + (self.hitrect.width // 2)

  def moveright(self):
    self.pos[0] += 8
    self.hitrect.center = self.pos
    if self.hitrect.right > c.WIDTH:
      self.pos[0] = c.WIDTH - (self.hitrect.width // 2)
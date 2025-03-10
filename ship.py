# Arden Boettcher
# 3/3/25
# Ship Class

import pygame as pg
import config as c
import projectiles as proj


class Ship:
  def __init__(self):
    self.ship = pg.image.load("sprites/Ship.png")
    self.ship.convert_alpha()
    self.pos = [100, 100]
    self.rect = self.ship.get_rect()
    self.hitrect = pg.Rect(0, 0, 25, 25)
    self.firing_speed = 100
    self.firing_timer = 0
    self.firing_side = 10

    self.rect.center = self.pos
    self.hitrect.center = self.pos


  def draw(self, surface: pg.Surface):
    self.hitrect.center = self.pos
    self.rect.center = self.pos
    pg.draw.rect(surface, c.RED, self.hitrect, 2)
    surface.blit(self.ship, self.rect)


  def check_movement(self, dt):
    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
      self.moveup(dt)
    if keys[pg.K_DOWN]:
      self.movedown(dt)
    if keys[pg.K_LEFT]:
      self.moveleft(dt)
    if keys[pg.K_RIGHT]:
      self.moveright(dt)

  def events(self, event):
    # if event.type == pg.KEYDOWN:
    #   if event.key == pg.K_SPACE:
    #     self.fire()
    pass


  def fire(self):
    print("pew")


  def moveup(self, dt):
    self.pos[1] -= 250 * dt
    self.hitrect.center = self.pos
    if self.hitrect.top < 0:
      self.pos[1] = 0 + (self.hitrect.height // 2)

  def movedown(self, dt):
    self.pos[1] += 250 * dt
    self.hitrect.center = self.pos
    if self.hitrect.bottom > c.HEIGHT:
      self.pos[1] = c.HEIGHT - (self.hitrect.height // 2)

  def moveleft(self, dt):
    self.pos[0] -= 250 * dt
    self.hitrect.center = self.pos
    if self.hitrect.left < 0:
      self.pos[0] = 0 + (self.hitrect.width // 2)

  def moveright(self, dt):
    self.pos[0] += 250 * dt
    self.hitrect.center = self.pos
    if self.hitrect.right > c.WIDTH:
      self.pos[0] = c.WIDTH - (self.hitrect.width // 2)

  def update_firetimer(self, dt) -> bool:
    self.firing_timer += self.firing_speed * dt
    return self.firing_timer >= 10

  def fire(self, group):
    temp_pos = self.pos.copy()
    temp_pos[0] += self.firing_side
    proj.Projectile(group, temp_pos, c.GREEN, -1000, 5)
    self.firing_side *= -1
    self.firing_timer -= 10
# Arden Boettcher
# 3/3/25
# Ship Class

import pygame as pg
import config as c
import projectiles as proj
import particles as part
from random import randint


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
    self.bullet_color = c.RED

    self.rect.center = self.pos
    self.hitrect.center = self.pos

    self.hit_timer = 0

  def update(self, dt, group):
    self.check_movement(dt)
    self.check_firing(dt, group)
    self.hit_timer -= dt

  def draw(self, surface: pg.Surface):
    self.hitrect.center = self.pos
    self.rect.center = self.pos
    # pg.draw.rect(surface, c.RED, self.hitrect, 2)
    surface.blit(self.ship, self.rect)

  def check_firing(self, dt, group):
    if pg.key.get_pressed()[pg.K_i]:
      if self.update_firetimer(dt):
        self.fire(group)

  def check_movement(self, dt):
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
      self.moveup(dt)
    if keys[pg.K_s]:
      self.movedown(dt)
    if keys[pg.K_a]:
      self.moveleft(dt)
    if keys[pg.K_d]:
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
    temp_pos[1] += 10
    temp_pos[0] += self.firing_side
    self.bullet_color = c.rainbow(self.bullet_color, 10)
    proj.Projectile(group, temp_pos, self.bullet_color, 1000, 5, (4, 6))
    self.firing_side *= -1
    self.firing_timer -= 10

  # def dash(self, dt):

  def hit(self, group):
    if self.hit_timer <= 0:
      part.Explosion(group, self.pos.copy(), c.WHITE, 0, 20, 8)
      for x in range(10):
        part.Rainbow_Slowed_Part(group, self.pos.copy(), c.RED, c.rand_vector(), randint(180, 220), 300)
      self.hit_timer = 0.5
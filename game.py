# Arden Boettcher
# 3/3/25
# Game Class

import pygame as pg
import ship
import particles as part
import projectiles as proj
import enemies as e

class Game:
  def __init__(self):
    self.player = ship.Ship()
    self.friendly_proj: list[proj.Projectile] = []
    self.enemy_proj: list[proj.Projectile] = []
    self.enemies: list[e.Enemy] = []
    self.particle_group = pg.sprite.Group()

  def update(self, dt):
    self.particle_group.update(dt)

    for proj in self.friendly_proj:
      for enemy in self.enemies:
        if enemy.is_hit(proj):
          enemy.hit(proj)
          self.spawn_explosion(proj.pos, 10)
          del proj

    for enemy in self.enemies:
      enemy.update(dt)
      if not enemy.alive:
        self.kill(enemy)
        del enemy

  def spawn_explosion(self, pos, size, color):
    part.Explosion(self.particle_group, pos, color, 0, size)


  def kill(self, object):
    self.spawn_explosion(object.pos, 40)

  def events(self, event):
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        self.friendly_proj.append()

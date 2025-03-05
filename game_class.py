# Arden Boettcher
# 3/3/25
# Game Class

import pygame as pg
import ship
import particles as part
import projectiles as proj
import enemies as e
import config as c

from random import randint

class Game:
  def __init__(self):
    self.player = ship.Ship()
    self.friendly_proj_group: pg.sprite.Group[proj.Projectile] = pg.sprite.Group()
    self.enemy_proj: list[proj.Projectile] = []
    self.enemies: pg.sprite.Group[e.Enemy] = pg.sprite.Group()
    self.particle_group: pg.sprite.Group[part.Particle] = pg.sprite.Group()

  def update(self, dt):
    self.player.check_movement()

    self.particle_group.update(dt)
    self.friendly_proj_group.update(dt)

    for proj in self.friendly_proj_group:
      for enemy in self.enemies:
        if enemy.is_hit(proj):
          enemy.hit(proj)
          self.spawn_explosion(proj.pos, 10, c.WHITE, 5)
          proj.kill()

    for enemy in self.enemies:
      enemy.update(dt)
      if not enemy.alive:
        self.kill(enemy)
        enemy.kill()

  def spawn_explosion(self, pos, size, color, weight):
    part.Explosion(self.particle_group, pos, color, 0, size, weight)


  def kill(self, object: e.Enemy):
    self.spawn_explosion(list(object.hitrect.center), 40, c.WHITE, 8)
    part.Particle(self.particle_group, object.pos.copy(), c.WHITE, pg.math.Vector2(randint(-100, 100) / 100, randint(-100, 100) / 100), 100, 50)


  def events(self, event):
    self.player.events(event)
    self.player.check_movement()

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        proj.Projectile(self.friendly_proj_group, self.player.pos.copy(), c.BLUE, -1000, 5)

      if event.key == pg.K_s:
        e.Enemy(self.enemies, [40, 40])



  def draw(self, surface):
    self.player.draw(surface)

    for proj in self.friendly_proj_group:
      proj.draw(surface)

    for proj in self.enemy_proj:
      proj.draw(surface)

    for enemy in self.enemies:
      enemy.draw(surface)

    self.particle_group.draw(surface)
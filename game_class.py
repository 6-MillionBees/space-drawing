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
    self.player.update(dt, self.friendly_proj_group)

    self.particle_group.update(dt)
    self.friendly_proj_group.update(dt)

    for enemy in self.enemies:
      if self.player.hitrect.colliderect(enemy.hitrect):
        self.player.hit(self.particle_group)

    for proj in self.friendly_proj_group:
      for enemy in self.enemies:
        if enemy.is_hit(proj):
          enemy.hit(proj)
          self.spawn_explosion(proj.pos, 10, c.WHITE, 5)
          proj.kill()
          if not enemy.alive:
            self.kill(enemy)
            enemy.kill()
          break

    self.enemies.update(dt)



  def spawn_explosion(self, pos, size, color, weight):
    part.Explosion(self.particle_group, pos, color, 0, size, weight)


  def kill(self, object: e.Enemy):
    self.spawn_explosion(list(object.hitrect.center), 40, c.WHITE, 8)
    for x in range(10):
      part.Rainbow_Slowed_Part(self.particle_group, object.pos.copy(), c.WHITE, c.rand_vector(), randint(80, 120), 100)


  def events(self, event: pg.event.Event):
    self.player.events(event)

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_i:
        self.player.fire(self.friendly_proj_group)
        self.player.firing_timer = 0

      if event.key == pg.K_p:
        e.Enemy(self.enemies, [40, 40])



  def draw(self, surface):
    self.player.draw(surface)

    for proj in self.friendly_proj_group:
      proj.draw(surface)

    for proj in self.enemy_proj:
      proj.draw(surface)

    for enemy in reversed(self.enemies.sprites()):
      enemy.draw(surface)

    for part in self.particle_group:
      part.draw(surface)

# Arden Boettcher
# 3/12/25
# Boss Testing

import pygame as pg
import config as c


class Lobster(pg.sprite.Sprite):
  def __init__(self, groups) -> None:
    super().__init__(groups)






class Lobster_arm(pg.sprite.Sprite):
  def __init__(self, groups, pos: int) -> None:
    super().__init__(groups)
    self.image: pg.Surface = pg.image.load("sprites/lobster_arm.png")
    self.overlay = pg.Surface(self.image.get_rect())
    self.pos = pos
    self.image_offset = c.rand_vector()
    self.image_pos = self.pos + self.image_offset
    self.hitrect = self.image.get_rect() # WIP

  def update(self, dt):
    self.offset_rotate(dt)


  def offset_rotate(self, dt):
    self.image_offset.rotate_ip(200 * dt)
    self.image_pos = self.pos + self.image_offset

  def hit(self):

  def get_hit(self, projectiles):

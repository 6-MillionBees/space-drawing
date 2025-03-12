# Arden Boettcher
# 3/12/25
# Boss Testing

import pygame as pg
from pygame.sprite import _Group


class Lobster(pg.sprite.Sprite):
  def __init__(self, groups) -> None:
    super().__init__(groups)

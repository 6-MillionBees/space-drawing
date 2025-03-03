# Arden Boettcher
# 3/3/25
# Lazer Class

class Lazer:
  def __init__(self, pos, color, friendly, speed):
    self.pos = pos
    self.color = color
    self.friendly = friendly
    self.speed = speed

  def update(self):
    self.pos[0] += self.speed
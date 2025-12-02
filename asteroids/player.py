from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player:
    def __init__(self, x, y, player_radius=PLAYER_RADIUS):
        self.x = x
        self.y = y
        self.radius = player_radius
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

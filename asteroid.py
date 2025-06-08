from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        blue_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(blue_angle)
        vec2 = self.velocity.rotate(-blue_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid1.velocity = vec1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid2.velocity = vec2 * 1.2
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, circle):
        """
        Detecting a collision between two circles is simple:

        We calculate the distance between the center of the two circles, let's call it distance
        Let's call the radius of one circle r1, and the radius of the other circle r2
        If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't.
        """
        distance = self.position.distance_to(circle.position)
        combined_radii = self.radius + circle.radius
        return distance <= combined_radii

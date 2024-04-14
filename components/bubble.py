class Bubble:
    def __init__(self):
        self.angle = None
        self.speed, self.speed_x, self.speed_y = None, None, None
        self.x, self.y = None, None
        self.radius = None
        self.shape()

    def shape(self):
        # Generate shape
        pass

    def update(self, speed_delta):
        # Update self params
        pass

    def draw(self, surface, screen):
        # Draw Bubble
        pass
class PointList:
    def __init__(self, points, screen):
        self.points = points
        self.screen = screen

    def connect_points(self):
        for i, point1 in enumerate(self.points):
            for point2 in self.points[i + 1:]:
                point1.connect(point2, self.screen)

    def move_points(self):
        for point in self.points:
            point.move()

    def draw_points(self):
        for point in self.points:
            point.draw(self.screen)

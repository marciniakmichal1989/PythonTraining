import pygame

class Drawer(object):
    def __init__(self, field_w, no_cols):
        super(Drawer, self).__init__()
        self.field_w = field_w
        self.no_cols = no_cols

    def drow_grid(self):
        x = y = 0

        for i in range(self.no_cols):
            x = self.field_w
            y += self.field_w
            for j in range(self.no_cols):
                from run import display

                pygame.draw.line(display, (0, 0, 0), [x, y], [x + self.field_w, y])
                pygame.draw.line(display, (0, 0, 0), [x + self.field_w, y], [x + self.field_w, y + self.field_w])
                pygame.draw.line(display, (0, 0, 0), [x + self.field_w, y + self.field_w], [x, y + self.field_w])
                pygame.draw.line(display, (0, 0, 0), [x, y + self.field_w], [x, y])

                pygame.display.update()
                x += self.field_w


class Grid(object):
    def __init__(self):
        super(Grid, self).__init__()


class GridDrawer(Drawer, Grid):
    def __init__(self, field_W, no_cols):
        Grid.__init__(self)
        Drawer.__init__(self, field_w=field_W, no_cols=no_cols)
        #super(GridDrower, self).__init__(height=2, width=3, number_of_fields=64, field_w=20)
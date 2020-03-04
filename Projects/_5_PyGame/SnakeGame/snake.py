from snake_part import snake_part

class snake:

    def __init__(self, xpos_head, ypos_head, xvel_head, yvel_head):

        self.body = []
        self.addBody(xpos_head, ypos_head, xvel_head, yvel_head)

    def addBody(self, xpos, ypos, xvel, yvel):
        part = snake_part(xpos, ypos, xvel, yvel)
        self.body.append(part)


from game_part import game_part

class snake:

    def __init__(self, xpos_head, ypos_head, xvel_head, yvel_head):

        self.body = []
        self.addBody(xpos_head, ypos_head, xvel_head, yvel_head)

    def addBody(self, xpos, ypos, xvel, yvel):
        part = game_part(xpos, ypos, xvel, yvel)
        self.body.append(part)

    def deleteBody(self):
        self.body.pop()


from game_part import game_part

class snake:

    def __init__(self, xpos_head, ypos_head):

        self.body = []
        self.addBody(xpos_head, ypos_head)

    def addBody(self, xpos, ypos):
        part = game_part(xpos, ypos)
        self.body.append(part)

    def deleteBody(self):
        self.body.pop()


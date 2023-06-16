from game.components.menu import Menu

class DeathMenu(Menu):
    def __init__(self, message, message_2, text_size=30):
        super().__init__(message, message_2, text_size)
        self.highest_score = 0

        

    def update_highest_score(self, score):
        if score > self.highest_score:
            self.highest_score = score












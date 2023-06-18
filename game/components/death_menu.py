from game.components.menu import Menu

class DeathMenu(Menu):
    def __init__(self, icon, message, message_2, message_3):
        super().__init__(icon, message, message_2, message_3, text_size=30)
        self.highest_score = 0


        

        

    def update_highest_score(self, score):
        if score > self.highest_score:
            self.highest_score = score












import pygame

from code import Level
from code.Menu import Menu
from code.const import menu_option





class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 450))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [menu_option[0], menu_option[1], menu_option[2]]:
                level = Level(self.window,'Level1', menu_return)
                level_return = level.run()
            elif menu_return == menu_option[3]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass



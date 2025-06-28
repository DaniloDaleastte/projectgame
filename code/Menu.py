import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import menu_option


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)

        selected_index = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=60, text="Nav game", text_color=(0, 0, 0), text_center_pos=((800 / 2), 100))

            for i in range(len(menu_option)):
                if i == selected_index:
                    self.menu_text(
                        text_size=30, text=menu_option[i], text_color=(0, 0, 0),
                        text_center_pos=((800 / 2), 200 + 35 * i))
                else:
                    self.menu_text(
                        text_size=30, text=menu_option[i], text_color=(255, 255, 255),
                        text_center_pos=((800 / 2), 200 + 35 * i))

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if selected_index < len(menu_option) - 1:
                            selected_index += 1
                        else:
                            selected_index = 0
                    if event.key == pygame.K_UP:
                        if selected_index > 0:
                            selected_index -= 1
                        else:
                            selected_index = len(menu_option) - 1
                    if event.key == pygame.K_RETURN:
                        return menu_option[selected_index]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

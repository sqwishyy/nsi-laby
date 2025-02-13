import pygame
from labyrinthe import Labyrinthe
from warfog import Warfog


def render(labyrinthe, taille_case, espace):
    renderFog = False
    pygame.init()
    warfog = Warfog(50)
    largeur = labyrinthe.largeur
    hauteur = labyrinthe.hauteur
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Labyrinthe')

    murs = labyrinthe.get_murs()
    player_pos = [largeur // 2, hauteur // 2]

    def can_move_to(new_pos):
        i, j = new_pos
        if i < 0 or i >= largeur or j < 0 or j >= hauteur:
            return False
        case = labyrinthe.laby[i][j]
        if player_pos[0] < i and case.murW:
            return False
        if player_pos[0] > i and case.murE:
            return False
        if player_pos[1] < j and case.murN:
            return False
        if player_pos[1] > j and case.murS:
            return False
        return True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_pos = list(player_pos)
                if event.key == pygame.K_LEFT:
                    new_pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    new_pos[0] += 1
                elif event.key == pygame.K_UP:
                    new_pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    new_pos[1] += 1
                elif event.key == pygame.K_f:
                    renderFog = not renderFog
                if can_move_to(new_pos):
                    player_pos = new_pos

        screen.fill((0, 0, 0))

        offset_x = screen_width // 2 - player_pos[0] * (taille_case + espace)
        offset_y = screen_height // 2 - player_pos[1] * (taille_case + espace)

        for mur in murs:
            (i, j), murN, murS, murW, murE = mur
            x = i * (taille_case + espace) + offset_x
            y = j * (taille_case + espace) + offset_y
            if murN:
                pygame.draw.line(screen, (255, 255, 255), (x, y), (x + taille_case, y))
            if murS:
                pygame.draw.line(screen, (255, 255, 255), (x, y + taille_case), (x + taille_case, y + taille_case))
            if murW:
                pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + taille_case))
            if murE:
                pygame.draw.line(screen, (255, 255, 255), (x + taille_case, y), (x + taille_case, y + taille_case))

        player_screen_x = screen_width // 2 + taille_case // 2
        player_screen_y = screen_height // 2 + taille_case // 2
        pygame.draw.circle(screen, (255, 0, 0), (player_screen_x, player_screen_y), taille_case // 2)

        if renderFog:
            warfog.render(screen, (player_screen_x, player_screen_y))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    labyrinthe = Labyrinthe(20, 20)
    labyrinthe.generer()
    render(labyrinthe, 20, 5)
import pygame

def main():
    """ Set up the game and run the main loop"""
    pygame.init()
    surface_sz = 480 # pixels

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    small_rect = (100, 200, 150, 50)
    RED = (255, 0, 0)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        main_surface.fill((0, 100, 255))

        main_surface.fill(RED, small_rect)

        pygame.display.flip()

    pygame.quit()
main()

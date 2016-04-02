import pygame
import time

def main():
    pygame.init()
    pygame.display.set_mode((640, 480))

    ball = pygame.image.load("tennis_ball.png")

    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1 - t0)
            t0 = t1

        main_surface.fill((0, 100, 255))
        main_surface.fill((0, 231, 0), 400, 300, 50, 60)

        main_surface.blit(ball, (100, 200))

        the_text = my_font.render("Frame = {0}\tFrame rate = {1:.2f} fps".
                   format(framecount, frame_rate), True, (0, 0, 0))

        main_surface.blit(the_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

main()

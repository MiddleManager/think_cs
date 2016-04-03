import pygame, math
pygame.init()

# Create a new surface and window
surface_sz = 1024
main_surface = pygame.display.set_mode((surface_sz,surface_sz))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):
    """ Draws a tree fractal pattern recursively """
    trunk_ratio = 0.29
    trunk = sz * trunk_ratio
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u,v) = posn
    new_pos = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, posn, new_pos)

    if order > 0: # Draw another layer of sub branches
        # Hack to make the major branches different colors
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

        # Make the recursive calls to draw the two subtrees
        newsz = sz*(1-trunk_ratio)
        draw_tree(order-1, theta, newsz, new_pos, heading-theta, color1, depth+1)
        draw_tree(order-1, theta, newsz, new_pos, heading+theta, color2, depth+1)

def gameloop():
    theta = 0
    while True:
        # Handle events from mouse keyboard joypad etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Updates the angle
        theta += 0.01

        # Draw everything
        main_surface.fill((255,255,0))
        draw_tree(9, theta, surface_sz*0.9, (surface_sz//2, surface_sz-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)



gameloop()
pygame.quit()

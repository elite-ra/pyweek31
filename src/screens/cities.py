import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
city_coords = [[(0, 0), (52, 20)], [(50, 50), (52, 20)], [(130, 60), (52, 20)], [(150, 300), (52, 20)],
               [(400, 200), (52, 20)], [(600, 500), (52, 20)]]
city_names = ['Agra', 'Delhi', 'Egypt', 'Pune', 'Pi', 'Hello']

example_dict = {k: ['-Condition1', '-Condition2', '-Condition3'] for k in city_names}

coin_limit = 50000


def city_name(name, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(name, True, (0, 0, 0))
    screen.blit(text, (x, y))


stats_showing = False

running = True
while running:

    screen.fill((0, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, a, b in zip([pygame.Rect(a, b) for [a, b] in city_coords], city_names, city_coords):
        pygame.draw.rect(screen, (0, 0, 0), i, 2)
        city_name(a, b[0][0] + 2, b[0][1] + 2, 18)
        if pygame.mouse.get_pressed()[0]:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if i.collidepoint(x, y) and not stats_showing:
                stats_showing = a
            if pygame.Rect((446, 480), (54, 20)).collidepoint(x, y) and stats_showing:
                stats_showing = False
        if pygame.mouse.get_pressed()[2]:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if i.collidepoint(x, y):
                # 'a' is the city name and this condition means that there was a right click on the city name
                # Change scene to chase
                pass

    if stats_showing:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((250, 100), (250, 400)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((250, 100), (250, 400)), 2)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(stats_showing, True, (0, 0, 0))
        w = text.get_rect().width
        screen.blit(text, (250 + (250 - w) / 2, 120))

        font = pygame.font.Font('freesansbold.ttf', 15)
        temp = 0
        for condition in example_dict[stats_showing]:
            text = font.render(condition, True, (0, 0, 0))
            screen.blit(text, (260, 150 + temp * 20))
            temp += 1

        #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((446, 480), (54, 20)))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((446, 480), (54, 20)), 1)
        city_name('Close', 448, 482, 18)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 550, 600, 50))
    font = pygame.font.Font('freesansbold.ttf', 15)
    current_coins = 25000
    text = font.render(f'Coins stolen({current_coins}/{coin_limit})', True, (255, 255, 255))
    w = text.get_rect().width
    screen.blit(text, (100 + (600 - w) / 2, 555))

    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(120, 575, 560, 10))
    pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(120, 575, (current_coins/coin_limit)*560, 10))

    pygame.display.update()

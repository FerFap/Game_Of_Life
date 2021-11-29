from GameOfLife import GameOfLife as Game
import pygame as py


def draw_grid(game, screen, offset_x, offset_y, width_block, height_block, width, height):
    white = (255, 255, 255)
    gray = (100, 100, 100)
    black = (0, 0, 0)

    for j in range(0, height, height_block):
        for i in range(0, width, width_block):
            py.draw.rect(screen, gray, (i, j, width_block, height_block), 1)

    for x, y in game.game:
        i = x * width_block + offset_x
        j = y * height_block + offset_y
        if 0 <= i < width and 0 <= j < height:
            py.draw.rect(screen, white, (i, j, width_block, height_block), 0)
            py.draw.rect(screen, black, (i, j, width_block, height_block), 1)


def main():
    main_clock = py.time.Clock()
    py.init()
    width = 1700
    height = 1000
    black = (0, 0, 0)
    screen = py.display.set_mode((width, height), py.RESIZABLE)
    width_block = 25
    height_block = 25
    offset_x = 0
    offset_y = 0
    run = True
    rows = width // width_block
    cols = height // height_block
    game = Game(rows, cols, int(rows * cols * 0.6))
    
    update = True
    fps = 45
    d_x = 0
    d_y = 0
    count = 0
    refresh = 20
    mouse_mode = 0
    while run:
        count += 1
        screen.fill(black)
        if update and not count % refresh:
            game.update()
        draw_grid(game, screen, offset_x, offset_y, width_block, height_block, width, height)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    update = not update
                if event.key == py.K_r:
                    game.game.clear()
                if event.key == py.K_g:
                    start_x = -offset_x // width_block
                    start_y = -offset_y // height_block
                    rows = width // width_block
                    cols = height // height_block
                    game.generate_random(start_x, start_y, rows, cols)
                    del start_x, start_y, rows, cols
                if event.key == py.K_a:
                    d_x = width_block
                if event.key == py.K_d:
                    d_x = -width_block
                if event.key == py.K_w:
                    d_y = height_block
                if event.key == py.K_s:
                    d_y = -height_block
                if event.key == py.K_m:
                    refresh = max(5, refresh - 5)
                if event.key == py.K_l:
                    refresh = min(20, refresh + 5)
            if event.type == py.WINDOWRESIZED:
                width, height = screen.get_width(), screen.get_height()
            if event.type == py.KEYUP:
                if event.key == py.K_a:
                    d_x = 0
                if event.key == py.K_d:
                    d_x = 0
                if event.key == py.K_w:
                    d_y = 0
                if event.key == py.K_s:
                    d_y = 0
            if event.type == py.MOUSEBUTTONDOWN:
                mouse_mode = event.button
            if event.type == py.MOUSEBUTTONUP:
                mouse_mode = 0
        if mouse_mode:
            (x, y) = py.mouse.get_pos()
            tup = ((x - offset_x) // width_block, (y - offset_y) // height_block)
            if mouse_mode == 1:
                game.game.add(tup)
            elif mouse_mode == 3:
                if tup in game.game:
                    game.game.remove(tup)
        offset_x += d_x
        offset_y += d_y
        py.display.update()
        main_clock.tick(fps)
    py.quit()


main()

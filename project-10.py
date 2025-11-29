import pygame

pygame.init()

w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Tic Tac Toe")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.Font(None, 120)
small = pygame.font.Font(None, 50)
cell = 200

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
winner = None
over = False

def check():
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return board[r][0]

    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return board[0][c]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    for r in board:
        if "" in r:
            return None
    return "Draw"

def reset():
    global board, player, winner, over
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = "X"
    winner = None
    over = False

run = True
while run:
    screen.fill(white)

    pygame.draw.line(screen, black, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, black, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 5)

    for r in range(3):
        for c in range(3):
            if board[r][c] != "":
                t = font.render(board[r][c], True, black)
                screen.blit(t, (c * 200 + 60, r * 200 + 50))

    if winner == "Draw":
        m = small.render("Draw! Press R to restart", True, red)
        screen.blit(m, (60, 260))
    elif winner:
        m = small.render(winner + " wins! Press R to restart", True, red)
        screen.blit(m, (60, 260))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()

        if event.type == pygame.MOUSEBUTTONDOWN and not over:
            x, y = pygame.mouse.get_pos()
            r = y // 200
            c = x // 200

            if board[r][c] == "":
                board[r][c] = player
                res = check()
                if res:
                    winner = res
                    over = True
                else:
                    player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()

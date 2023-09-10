"""
This is our my main driver file. It will be responsible for handling user 
input and displaying the current GameState object
"""
import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animation
IMAGES = {}

'''
Initialize a Global Dictionary of Images. This will be called exactly once in the main class
'''
def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("sprites/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #access an image by using dictionary by saying 'IMAGES['wp']'


'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT)) #look to add side panel with moves later on
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #flag variable for when a move is made

    load_images() #only do once before while loop
    running = True
    sqSelected = () #no square is highlighted initially, keep track of last click of the user (tuple: (row, col))
    playerClicks = [] #keep track of player clicls (two tuples: [(6,4), (4,4)])
    

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse handlers
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col): #the user clicked the same square twice
                    sqSelected = () #deselected
                    playerClicks = [] #clears player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for both 1st & 2nd clicks
                if len(playerClicks) == 2: #after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True
                            sqSelected = () #reset selected square
                            playerClicks = [] #resets user clicks
                    if not moveMade:
                        playerClicks = [sqSelected]
            #key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True
    
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highlights or move suggestion (later)
    drawPieces(screen, gs.board) #draw pieces on top of the squares

'''
Draw the squares on the board. The top left square is always light
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("light blue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect((c * SQ_SIZE), (r * SQ_SIZE), SQ_SIZE, SQ_SIZE))
            
'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], p.Rect((c * SQ_SIZE), (r * SQ_SIZE), SQ_SIZE, SQ_SIZE)) 
                #could be done in other function but separated so we can add highlights later (not too cost efficient for runtime)


if __name__ == "__main__":
    main()
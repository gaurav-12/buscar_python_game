import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTS ~~~~~~~~~~
#-------------- DISPLAY -----------------------------------------
Display = pygame.display.Info()
SCR_HEIGHT = Display.current_h
SCR_WIDTH = Display.current_w
DISPLAYSURF = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Battleship')
#----------------------------------------------------------------
SEL_BOX_LIST = [] # List of selected boxes.
BOARD_HEIGHT = 4 # number of rows in board
BOARD_WIDTH = 4 # number of columns in board
#SEL_BOXSIZE = 70 # length and breadth of selected box
BOXSIZE = 80 # length and breadth of box
GAPSIZE = 5 # gap b/w boxes
START_FONT_SIZE = 50 # Font size for 'StartButton' text
INSTRUC_FONT_SIZE = 20 # Font size for 'InstrucButton' text
XMARGIN = int((SCR_WIDTH - (BOARD_WIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((SCR_HEIGHT - (BOARD_HEIGHT * (BOXSIZE + GAPSIZE))) / 2)
ACTIVE_BOX = []
#----COLORS------
BOX_COLOR = (255,0,0)
START_COLOR = (0, 0, 255)
INSTRUC_COLOR = (0, 0, 0)
SEL_BOX_COLOR = (41, 41, 41)
BGCOLOR = (30, 30, 30) 
GREEN = (0,255,0)
BLUE = (0,0,255)
HOVER_COLOR = (41,41,41)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#----------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def CreateBoard(height, width): # creating board
    board = []
    for x in range(height):
        board.append(["0"] * width)
    n = 1
    for row in board:
        for box in range(width):
            row[box] = n
            n+=1
    return board

# Example of Board --- Here is board of height 2 and width 4 ---- [[1, 2, 3, 4], [5, 6, 7, 8]]

def RowColOf(box,board): # getting row and column number of a box in board
    boxRow = 0
    boxCol = 0
    for scanRow in board: # iterate through board ---- gives row
        boxRow +=1 # row will increase as we iterate through board
        boxCol = 0 # after completing each row we come back to first column of next row
        for scanBox in scanRow: # iterate through row ---- gives box
            boxCol+=1 # column will increase as we iterate through row
            if scanBox == box:
                return (boxRow, boxCol)

def LeftTopOf(box, board): # getting left top coordinates of a box in board
    boxRow , boxCol = RowColOf(box,board)    
    left = ((boxCol * (BOXSIZE + GAPSIZE)) - (BOXSIZE + GAPSIZE)) + XMARGIN
    top = ((boxRow * (BOXSIZE + GAPSIZE)) - (BOXSIZE + GAPSIZE)) + YMARGIN
    return (left,top)            
    
def DrawBoard(board, SEL_BOX_LIST, x = 'default'): # drawing board
    if x == 'default':
        for row in board:
            for box in row:
                left,top = LeftTopOf(box, board)
                ThisBox = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                if ThisBox in SEL_BOX_LIST:
                    pygame.draw.rect(DISPLAYSURF,SEL_BOX_COLOR,(left,top,BOXSIZE, BOXSIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, BOXSIZE, BOXSIZE))
    elif x == 'start':
        for row in board:
            for box in row:
                left,top = LeftTopOf(box, board)
                ThisBox = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
                if ThisBox in SEL_BOX_LIST:
                    pygame.draw.rect(DISPLAYSURF,SEL_BOX_COLOR,(left,top,BOXSIZE, BOXSIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, BOXSIZE, BOXSIZE))
                    pygame.display.update()
                    pygame.time.wait(150)
                

def DrawStartButton(x = False): # Do not draw button unless x is given true.
    # Placing start button.
    left = SCR_WIDTH/2
    top = SCR_HEIGHT/2 + 30
    StartButton = pygame.Rect(left-100,top-40, 200, 80)
    if not x: # when x is false give StartButton's rect.
        return StartButton
    else: # otherwise draw it
        for size in range(25): # First animation. (Of resizing start button's background)
            #--------------------- TOP - LEFT of surface (which enlarge during the loop)-----
            left = SCR_WIDTH/2
            top = SCR_HEIGHT/2 + 30
            #--------------------------------------------------------------------------------
            #pygame.time.wait(10)
            width = 200 + size # Width of surface increases after every loop...
            height = 80 + size #...and same for height
            BG = pygame.Surface((width, height))
            BG.fill((0,0,0))
            left = left - (width/2) #------ Here TOP - LEFT are adjusting with increase in size -
            top = top - (height/2)
            DISPLAYSURF.blit(BG, (left,top))
            #------------------------- Drawing Start Button --------------
            START_COLOR = (255,0,0)
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, StartButton)
            pygame.draw.rect(DISPLAYSURF, START_COLOR, StartButton)
            FontObj_Start = pygame.font.Font('PoplarStd.otf', START_FONT_SIZE)
            StartButtonText = FontObj_Start.render('START', True, WHITE, START_COLOR)
            StartButtonText_Rect = StartButtonText.get_rect()
            StartButtonText_Rect.center = StartButton.center
            DISPLAYSURF.blit(StartButtonText, StartButtonText_Rect)
            pygame.display.update()
            #--------------------------------------------------------------
        for size in range(25): # Second animation. (Of hiding the enlarged background)
            #--------------------- TOP - LEFT of surface (which enlarge during the loop)-----
            left = SCR_WIDTH/2
            top = SCR_HEIGHT/2 + 30
            #--------------------------------------------------------------------------------
            #pygame.time.wait(10)
            width = 200 + size # Width of surface increases after every loop...
            height = 80 + size #...and same for height
            BG = pygame.Surface((width, height))
            BG.fill(BGCOLOR)
            left = left - (width/2) #------ Here TOP - LEFT are adjusting with increase in size -
            top = top - (height/2)
            DISPLAYSURF.blit(BG, (left,top))
            #------------------------- Drawing Start Button --------------
            START_COLOR = (255,0,0)
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, StartButton)
            pygame.draw.rect(DISPLAYSURF, START_COLOR, StartButton)
            FontObj_Start = pygame.font.Font('PoplarStd.otf', START_FONT_SIZE)
            StartButtonText = FontObj_Start.render('START', True, WHITE, START_COLOR)
            StartButtonText_Rect = StartButtonText.get_rect()
            StartButtonText_Rect.center = StartButton.center
            DISPLAYSURF.blit(StartButtonText, StartButtonText_Rect)
            pygame.display.update()
            #--------------------------------------------------------------

def DrawInstrucButton(x = False): # Do not draw button unless x is given true.
    # Placing start button.
    left = SCR_WIDTH/2
    top = SCR_HEIGHT/2 + 140
    InstrucButton = pygame.Rect(left-70,top-30, 140, 60)
    if not x: # when x is false give StartButton's rect.
        return InstrucButton
    elif x == 'hover': # if x  = 'hover' thendraw hover box.
        for size in range(25): # First animation. (Of resizing start button's background)
            #--------------------- TOP - LEFT of surface (which enlarge during the loop)-----
            left = SCR_WIDTH/2
            top = SCR_HEIGHT/2 + 140
            #--------------------------------------------------------------------------------
            width = 130 + size # Width of surface increases after every loop...
            height = 50 + size #...and same for height
            BG = pygame.Surface((width, height))
            BG.fill((0,0,0))
            left = left - (width/2) #------ Here TOP - LEFT are adjusting with increase in size -
            top = top - (height/2)
            DISPLAYSURF.blit(BG, (left,top))
            #------------------------- Drawing Instruc Button --------------
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, InstrucButton)
            pygame.draw.rect(DISPLAYSURF, INSTRUC_COLOR, InstrucButton)
            FontObj_Instruc = pygame.font.Font('PoplarStd.otf', INSTRUC_FONT_SIZE)
            InstrucButtonText = FontObj_Instruc.render('INSTRUCTIONS', True, WHITE, INSTRUC_COLOR)
            InstrucButtonText_Rect = InstrucButtonText.get_rect()
            InstrucButtonText_Rect.center = InstrucButton.center
            DISPLAYSURF.blit(InstrucButtonText, InstrucButtonText_Rect)
            pygame.display.update()
            #--------------------------------------------------------------
        for size in range(25): # First animation. (Of resizing start button's background)
            #--------------------- TOP - LEFT of surface (which enlarge during the loop)-----
            left = SCR_WIDTH/2
            top = SCR_HEIGHT/2 + 140
            #--------------------------------------------------------------------------------
            #pygame.time.wait(10)
            width = 130 + size # Width of surface increases after every loop...
            height = 50 + size #...and same for height
            BG = pygame.Surface((width, height))
            BG.fill(BGCOLOR)
            left = left - (width/2) #------ Here TOP - LEFT are adjusting with increase in size -
            top = top - (height/2)
            DISPLAYSURF.blit(BG, (left,top))
            #------------------------- Drawing Instruc Button --------------
            pygame.draw.rect(DISPLAYSURF, BGCOLOR, InstrucButton)
            pygame.draw.rect(DISPLAYSURF, INSTRUC_COLOR, InstrucButton)
            FontObj_Instruc = pygame.font.Font('PoplarStd.otf', INSTRUC_FONT_SIZE)
            InstrucButtonText = FontObj_Instruc.render('INSTRUCTIONS', True, WHITE, INSTRUC_COLOR)
            InstrucButtonText_Rect = InstrucButtonText.get_rect()
            InstrucButtonText_Rect.center = InstrucButton.center
            DISPLAYSURF.blit(InstrucButtonText, InstrucButtonText_Rect)
            pygame.display.update()
            #--------------------------------------------------------------
    elif x: # when x is given True otherwise draw it
        #--------------------- TOP - LEFT of surface (which enlarge during the loop)-----
        left = SCR_WIDTH/2
        top = SCR_HEIGHT/2 + 140
        #--------------------------------------------------------------------------------
        #------------------------- Drawing Instruc Button --------------
        START_COLOR = (0,0,0)
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, InstrucButton)
        pygame.draw.rect(DISPLAYSURF, INSTRUC_COLOR, InstrucButton)
        FontObj_Instruc = pygame.font.Font('PoplarStd.otf', INSTRUC_FONT_SIZE)
        InstrucButtonText = FontObj_Instruc.render('INSTRUCTIONS', True, WHITE, INSTRUC_COLOR)
        InstrucButtonText_Rect = InstrucButtonText.get_rect()
        InstrucButtonText_Rect.center = InstrucButton.center
        DISPLAYSURF.blit(InstrucButtonText, InstrucButtonText_Rect)
        pygame.display.update()
        #--------------------------------------------------------------

def IntroPage(): # Page shown when game is started.
    INTRO_FONT_SIZE = 100 # Font size for 'Battleship' text
    FontObj = pygame.font.Font('gomarice_kaiju_monster.ttf', INTRO_FONT_SIZE)        
    LetsPlayBattleship = FontObj.render("Battleship!", True, GREEN, BGCOLOR)
    LetsPlayBattleship_Rect = LetsPlayBattleship.get_rect()
    LetsPlayBattleship_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT/2-90)
    DISPLAYSURF.blit(LetsPlayBattleship, LetsPlayBattleship_Rect)
    pygame.display.update()
    DrawInstrucButton(True)
    DrawStartButton(True)

def DrawInstrucBox(x = 'ON'):
    if x == 'ON':
        # Transparent Overlay---------------------------------------------------------
        for alpha in range(30):
            Overlay = pygame.Surface((SCR_WIDTH, SCR_HEIGHT))  # the size of your rect
            Overlay.set_alpha(alpha)                # alpha level
            Overlay.fill(RED)           # this fills the entire surface
            DISPLAYSURF.blit(Overlay, (0,0))    # (0,0) are the top-left coordinates
            pygame.display.update()
        #-----------------------------------------------------------------------------
        TextImage = pygame.image.load('Instructions.png')
        DISPLAYSURF.blit(TextImage, (SCR_WIDTH/2-400,60))
        pygame.display.update()
    elif x == 'OFF':
        DISPLAYSURF.fill(BGCOLOR)
        IntroPage()

def RandomRow(board):
    return randint(1, len(board))

def RandomCol(board):
    return randint(1, len(board[0]))

def MouseHoverSomeBox (mousex, mousey, board): # check if mouse was hovered...
    #...over any box.
    for row in board: # each row
        for box in row: # each box
            left,top = LeftTopOf(box, board)
            AnyBox = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if AnyBox.collidepoint(mousex, mousey): # check if mouse collided with any box
                return True 

    

def MouseCollideSomeBox(mousex, mousey, board): # check if mouse collided...
    #...with any box.
    for row in board: # each row
        for box in row: # each box
            left,top = LeftTopOf(box, board)
            AnyBox = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if AnyBox in SEL_BOX_LIST: # If clicked selected box, don't do anything...
                pass
            else: # otherwise return True.
                if AnyBox.collidepoint(mousex, mousey): # check if mouse collided with any box
                    SEL_BOX_LIST.append(AnyBox) # then append it into SEL_BOX_LIST.
                    return True 

def MouseCollideOurBox(mousex, mousey, board, OurRow, OurCol): # check if mouse collided...
    #...with our box.
    for row in board: # each row
        for box in row: # each box
            left,top = LeftTopOf(box, board)
            AnyBox = (pygame.Rect(left, top, BOXSIZE, BOXSIZE))
            if AnyBox.collidepoint(mousex, mousey): # check if mouse collided with any box
                if RowColOf(box, board) == (OurRow, OurCol): # now check if box was our box
                    return True                



def DrawHoverBox(mousex, mousey, board):#Draw hover box over a box viz. under mouse coordinates
    for row in board:
        for box in row:
            left,top = LeftTopOf(box, board)
            AnyBox = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if AnyBox.collidepoint(mousex, mousey): # if we come up with our box..
                #...draw hover box over it.
                if AnyBox in SEL_BOX_LIST: # If hovered over selected box, don't do anything...
                    pass
                else: # otherwise Draw hover box.
                    pygame.draw.rect(DISPLAYSURF, HOVER_COLOR, (left, top, BOXSIZE, BOXSIZE))
                    pygame.display.update()
                return None # just to stop the box loop and row loop.

def GameOverAnimation():
    # Transparent Overlay---------------------------------------------------------
    for alpha in range(33):        
        Overlay = pygame.Surface((SCR_WIDTH, SCR_HEIGHT))  # the size of your rect
        Overlay.set_alpha(alpha)                # alpha level
        Overlay.fill(BLACK)           # this fills the entire surface
        DISPLAYSURF.blit(Overlay, (0,0))    # (0,0) are the top-left coordinates
        pygame.display.update()
    #-----------------------------------------------------------------------------
    GAME_OVER_SIZE = 90 # Font size for 'GameOver' text
    FontObj_Won = pygame.font.Font('PoplarStd.otf', GAME_OVER_SIZE)
    GameOverText = FontObj_Won.render('GAME OVER', True, RED)
    GameOverText_Rect = GameOverText.get_rect()
    GameOverText_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT/2)
    YOU_LOSE_SIZE = 50
    FontObj_Won = pygame.font.Font('PoplarStd.otf', YOU_LOSE_SIZE)
    YouLoseText = FontObj_Won.render('YOU LOSE', True, RED)
    YouLoseText_Rect = YouLoseText.get_rect()
    YouLoseText_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT/2+90)
    DISPLAYSURF.blit(YouLoseText, YouLoseText_Rect)
    DISPLAYSURF.blit(GameOverText, GameOverText_Rect)
    pygame.display.update()
    del SEL_BOX_LIST [:] # Empty SEL_BOXL_IIST when game is over..
    
def GameWonAnimation():
    # Transparent Overlay---------------------------------------------------------
    for alpha in range(30):        
        Overlay = pygame.Surface((SCR_WIDTH, SCR_HEIGHT))  # the size of your rect
        Overlay.set_alpha(alpha)                # alpha level
        Overlay.fill(RED)           # this fills the entire surface
        DISPLAYSURF.blit(Overlay, (0,0))    # (0,0) are the top-left coordinates
        pygame.display.update()
    #-----------------------------------------------------------------------------
    GAME_WON_SIZE = 90 # Font size for 'GameOver' text
    FontObj_Over = pygame.font.Font('PoplarStd.otf', GAME_WON_SIZE)
    GameWonText = FontObj_Over.render('YOU WON', True, WHITE)
    GameWonText_Rect = GameWonText.get_rect()
    GameWonText_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT/2)
    DISPLAYSURF.blit(GameWonText, GameWonText_Rect)
    pygame.display.update()
    del SEL_BOX_LIST [:] # Empty SEL_BOXL_IIST when game is over..
    pygame.time.wait(1500)

def PrintChance(x):
    CHANCE_SIZE = 50 # Font size for 'GameOver' text
    FontObj_Chance = pygame.font.Font('SHOWG.ttf', CHANCE_SIZE)
    ChanceText = FontObj_Chance.render('CHANCE :'+str(x), True, WHITE)
    ChanceText_Rect = ChanceText.get_rect()
    ChanceText_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT - 50)
    DISPLAYSURF.blit(ChanceText, ChanceText_Rect)
    #pygame.display.update()

def Enter_TextAnimation():
    ENTER_TEXTSIZE = 20
    FontObj_1 = pygame.font.Font('freesansbold.ttf', ENTER_TEXTSIZE)
    COLOR = (10, 10, 10) 
    EnterText = FontObj_1.render("Press 'ENTER' or Click on 'START' to Start the game", True, COLOR, BGCOLOR)
    EnterText_Rect = EnterText.get_rect()
    EnterText_Rect.center = (SCR_WIDTH/2, SCR_HEIGHT-150)
    DISPLAYSURF.blit(EnterText, EnterText_Rect)
    pygame.display.update()


assert BOARD_WIDTH == BOARD_HEIGHT # Board needs to have an equal number of boxes.
board = CreateBoard(BOARD_HEIGHT, BOARD_WIDTH) # Here is our board.

while True: # Main Game Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    OurRow = RandomRow(board)
    OurCol = RandomCol(board)
    START_BUTTON_ON = False # Initially StartButton is 'OFF'
    chance = 1
    if not START_BUTTON_ON: # Animate intro animation if START_BUTTON is not 'ON'
        DISPLAYSURF.fill(BGCOLOR) # Coloring the window background 
        #----------------Starting intro animation---------
        IntroPage() # Drawing Intro page
        pygame.display.update()
        #-------------------------------------------------
    mousex = 0
    mousey = 0
    while not START_BUTTON_ON: # Loop unless Start Button is clicked.
        IntroPage() # Drawing Intro page
        INSTRUC_BOX = 'OFF'
        Enter_TextAnimation()
        InstrucButton_Rect = DrawInstrucButton()
        StartButton_Rect = DrawStartButton()
        if InstrucButton_Rect.collidepoint(mousex, mousey):
            while InstrucButton_Rect.collidepoint(mousex, mousey):
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = event.pos
                    elif event.type == MOUSEBUTTONUP: # If button was clicked..
                        mousex, mousey = event.pos
                        if InstrucButton_Rect.collidepoint(mousex, mousey): #..check if..
                            #..InstrucButton was clicked
                            DrawInstrucBox()
                            INSTRUC_BOX = 'ON'
                            while INSTRUC_BOX == 'ON':
                                for event in pygame.event.get(): # Checking each event happening on window.
                                    if event.type == MOUSEBUTTONUP: # If button was clicked..
                                        INSTRUC_BOX = 'OFF'
                                        DrawInstrucBox('OFF')
                                        mousex = 0
                                        mousey = 0
                    
                DrawInstrucButton('hover')
        for event in pygame.event.get(): # Checking each event happening on window.
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == KEYUP and event.key == K_RETURN: # If Enter was pressed.
                START_BUTTON_ON = True # Now Start Button is 'ON'
            elif event.type == MOUSEBUTTONUP: # If button was clicked..
                mousex, mousey = event.pos
                if StartButton_Rect.collidepoint(mousex, mousey): #..check if StartButton..
                    #...was clicked
                    START_BUTTON_ON = True # Now Start Button is 'ON'
    BOARD_WIDTH = 4
    x = 'start'
    DISPLAYSURF.fill(BGCOLOR)
    DrawBoard(board, SEL_BOX_LIST, x) # Draw Board..
    while START_BUTTON_ON: # Finally Start Button is clicked (or, it is 'ON').
        XMARGIN = int((SCR_WIDTH - (BOARD_WIDTH * (BOXSIZE + GAPSIZE))) / 2)
        YMARGIN = int((SCR_HEIGHT - (BOARD_HEIGHT * (BOXSIZE + GAPSIZE))) / 2)
        mouseClicked = False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #~~~~~~~~~~~~~~CHEAT~~~~~~~~~~~~~
            elif (event.type == KEYUP and event.key == K_a):
                left = (OurCol * (BOXSIZE + GAPSIZE) - (BOXSIZE + GAPSIZE)) + XMARGIN
                top = (OurRow * (BOXSIZE + GAPSIZE) - (BOXSIZE + GAPSIZE)) + YMARGIN
                Temp = HOVER_COLOR # Storing HOVER_COLOR in temporary variable
                HOVER_COLOR = (200,0,0) # changing HOVER_COLOR(a bit light).
                DrawHoverBox(left, top, board)
                HOVER_COLOR = Temp # changing HOVER_COLOR back to previous value
                pygame.time.wait(60)
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                    mousex, mousey = event.pos
                    mouseClicked = True
        DISPLAYSURF.fill(BGCOLOR)
        PrintChance(chance)
        DrawBoard(board, SEL_BOX_LIST)
        if MouseHoverSomeBox(mousex, mousey, board): # if mouse hovers over some box.
            DrawHoverBox(mousex, mousey, board) # draw hover box over it.   
        if mouseClicked:
            print 'chance:',chance
            #~~~~~~~~~~~~~~CHEAT~~~~~~~~~~~~~
            print OurRow, OurCol
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if MouseCollideOurBox(mousex, mousey, board,OurRow, OurCol):
                OurRow = RandomRow(board)
                OurCol = RandomCol(board)
                temp = BOARD_WIDTH
                BOARD_WIDTH  += 2
                GameWonAnimation()
                board = CreateBoard(BOARD_HEIGHT, BOARD_WIDTH) # Here is our board.
                DrawBoard(board, SEL_BOX_LIST) # Draw Board..
            elif MouseCollideSomeBox(mousex, mousey, board):
                pygame.time.wait(200)
                if chance == 5:
                    GameOverAnimation()
                    pygame.time.wait(2000)
                    START_BUTTON_ON = False
                    break
                chance+=1
        pygame.display.update()

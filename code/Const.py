import pygame

# C
# COLORS

C_BLACK = (0, 0, 0) # BLACK
C_CYAN = (0, 128, 128) # CYAN
C_GREEN = (0, 128, 0) # GREEN
C_ORANGE = (255, 128, 0) # ORANGE
C_YELLOW = (255, 255, 128) # YELLOW
C_WHITE = (255, 255, 255) # WHITE

# E
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'MenuBg0': 0,
    'MenuBg1': 0,
    'MenuBg2': 0,
    'MenuBg3': 0,
    'MenuBg4': 0,
    'MenuBg5': 0,
    'MenuBg6': 0,
    'MenuBg7': 0,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player0': 0,
    'Player1': 0,
    'Player2': 0,
    'Player3': 0,
}

ENTITY_SCORE = {
    'MenuBg0' : 0,
    'MenuBg1' : 0,
    'MenuBg2' : 0,
    'MenuBg3' : 0,
    'MenuBg4' : 0,
    'MenuBg5' : 0,
    'MenuBg6' : 0,
    'MenuBg7' : 0,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player0': 0,
    'Player1': 0,
    'Player2': 0,
    'Player3': 0,
}

ENTITY_SPEED = {
    'MenuBg0' : 0,
    'MenuBg1' : 1,
    'MenuBg2' : 2,
    'MenuBg3' : 3,
    'MenuBg4' : 4,
    'MenuBg5' : 5,
    'MenuBg6' : 6,
    'MenuBg7' : 7,
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level1Bg7': 6,
    'Level1Bg8': 6,
    'Level1Bg9': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level3Bg4': 4,
    'Player0': 10,
    'Player1': 10,
    'Player2': 10,
    'Player3': 10,
}

ENTITY_HEALTH = {
    'MenuBg0' : 999,
    'MenuBg1' : 999,
    'MenuBg2' : 999,
    'MenuBg3' : 999,
    'MenuBg4' : 999,
    'MenuBg5' : 999,
    'MenuBg6' : 999,
    'MenuBg7' : 999,
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Player0': 0,
    'Player1': 0,
    'Player2': 0,
    'Player3': 0,
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = pygame.K_UP
PLAYER_KEY_DOWN = pygame.K_DOWN
PLAYER_KEY_SPACE = pygame.K_SPACE

# S
SPAWN_TIME = 500

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000
# W
WIN_WIDTH = 1366  # Width
WIN_HEIGHT = 768  # Height

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290)
             }
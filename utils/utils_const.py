class BubblyType(Enum):
    BIG_BUBBLE_AREA1 = 1
    SMALL_BUBBLE_BACKGROUND = 2
    MIDDLE_BUBBLE_AREA2 = 3


# Screen dimension
WIDTH, HEIGHT = 1245, 700

# Areas
BIG_BUBBLES_AREA = [((270, 510), (310, 10)),
                    ((310, 10), (860, 10)),
                    ((860, 10), (880, 110)),
                    ((880, 110), (550, 240)),
                    ((550, 240), (500, 400)),
                    ((500, 400), (910, 520)),
                    ((910, 520), (580, 550)),  # Bottom of teapot line
                    ((580, 550), (270, 510)),  # Bottom of teapot line
                    ]

SMALL_BUBBLES_AREA = [((885, 115), (555, 245)),
                      ((555, 245), (510, 395)),
                      ((510, 395), (910, 515)),
                      ((910, 515), (885, 115))
                      ]

TEAPOT_MAX_X = 910
TEAPOT_MIN_X = 270

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
ORANGE = (255, 165, 0)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 25, 25)

BLUE = (0, 0, 255)
TRANSPARENT_BLUE = (64, 128, 255, 64)  # 50% transparency (128/255)
from pygame import Color
from TextureData import TextureData

# Textuers
class Textures:
    CHECKPOINT_TEXTURE: TextureData

    @staticmethod
    def LoadStaticTextures():
        Textures.CHECKPOINT_TEXTURE = TextureData.load("Data/Images/checkpoint.png")

# Colors
WHITE:      Color = Color(255, 255, 255)
LIGHT_GRAY: Color = Color(200, 200, 200)
DARK_GRAY:  Color = Color( 75,  75,  75)
BLACK:      Color = Color(  0,   0,   0)
BLUE:       Color = Color(  0,   0, 255)
LIGHT_BLUE: Color = Color(175, 175, 255)
GREEN:      Color = Color(  0, 255,   0)
RED:        Color = Color(255,   0,   0)
DARK_RED:   Color = Color(200,   0,   0)
GOLD:       Color = Color(255, 215,   0)
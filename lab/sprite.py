# coding: utf-8
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty
from kivy.vector import Vector


class SpriteError(Exception):
    """To return specific error"""
    pass


class Sprite(Widget):
    """This class provide a simple sprite widget based on atlas,  mapping
    info in a dict with atlas keys in lists

    Keyword arguments:

    sprites_info -- is a dict with atlas keys list. See bellow:
            my_atlas_map = {
                "run": ["ryu_1", "ryu_2", "ryu_3"]
            }
            "run" Key is a name of animation and a list in key "run" is a atlas
            keys mapped to use on animation.


    atlas -- is a kivy atlas instance. The sprites_info lists keys must be a
        atlas keys

    """

    def __init__(self, sprites_info, atlas, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.num_sprites = 0
        # Sprite_sheet need to be reference of atlas keys and ids
        self.sprite_sheet = sprites_info
        # atlas to connect with sprite_sheet info
        self.atlas = atlas
        # to control animation speed
        self.sprite_fps = 2
        # to pause animation
        self.pause_frame = False
        # control flip but...
        self.flip = False

    def play(self, key, fps):
        """Play the animation selected by the key in dict passed in
        sprites arg
        """
        # Here use self.sprite_fps to control velocity of animation
        if fps % self.sprite_fps == 0:
            animation = self.sprite_sheet[key]
            sprite_len = len(animation) - 1
            if self.num_sprites > sprite_len:
                self.flip = False
                self.num_sprites = 0

            self.canvas.clear()
            if self.flip:                
                self.atlas[str(animation[self.num_sprites])].flip_horizontal()
                with self.canvas:
                    Rectangle(
                        texture=self.atlas[str(animation[self.num_sprites])],
                        pos=self.pos, size=self.size
                    )
            else:                
                with self.canvas:
                    Rectangle(
                        texture=self.atlas[str(animation[self.num_sprites])],
                        pos=self.pos, size=self.size
                    )

            if not self.pause_frame:
                self.num_sprites += 1

    def flip_h(self):
        self.flip = True
        self.num_sprites = 0


    def move(self):
        self.x = self.x + 10
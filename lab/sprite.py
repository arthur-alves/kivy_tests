# coding: utf-8
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty


class SpriteError(Exception):
    """To return specific error"""
    pass


class Sprite(Widget):
    """This class provide a simple sprite widget with animation loop
    Args:
        @atlas_path: caminho para atlas
        @sprite_sheet: (dict)
    """

    def __init__(self, sprites, atlas, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.sprite_sheet = sprites
        self.num_sprites = NumericProperty(0)
        self.atlas = atlas

    def play(self, key, dt):
        test = dt / 1000
        print int(test)
        if int(test % 2) == 0:
            animation = self.sprite_sheet[key]
            sprite_len = len(animation) - 1
            if self.num_sprites > (sprite_len):
                self.num_sprites = 0
            self.canvas.clear()
            with self.canvas:
                Rectangle(
                    texture=self.atlas[str(animation[self.num_sprites])]
                )
            self.num_sprites += 1

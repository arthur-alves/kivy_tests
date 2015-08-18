# coding: utf-8
from kivy.uix.widget import Widget
from kivy.atlas import Atlas
from kivy.graphics import Rectangle


class Sprite(Widget):
    """This class provide a simple sprite widget with animation loop
    Args:
        @atlas_path: caminho para atlas
        @sprite_sheet: (dict)
    """

    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.sprite_sheet = kwargs.get("sprite_sheet")
        self.num_sprites = 0
        self.atlas = Atlas("imgs/ryu.atlas")

    def play(self, key, dt):
        animation = self.sprite_sheet[key]
        sprite_len = len(animation)
        if self.num_sprites > (sprite_len - 1):
            self.num_sprites = 0
        self.canvas.clear()
        with self.canvas:
            Rectangle(
                texture=self.atlas[str(animation[self.num_sprites])],
                size=self.size, pos=self.pos
            )
        self.num_sprites += 1

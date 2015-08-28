# coding: utf-8
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty
from kivy.uix.image import Image


class SpriteError(Exception):
    """To return specific error"""
    pass


class Sprite(Widget):

    speed = NumericProperty(0)
    gravity = NumericProperty(1.5)
    jump_force = NumericProperty(20)
    num_sprites = NumericProperty(0)
    jumps = NumericProperty(2)

    def __init__(self, sprites_info, atlas, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        # Sprite_sheet need to be reference of atlas keys and ids
        self.sprite_sheet = sprites_info
        # atlas to connect with sprite_sheet info
        self.image = Image(source="", size=self.size)
        self.add_widget(self.image)
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
        self.image.pos = self.pos
        self.image.size = self.size
        if fps % self.sprite_fps == 0:
            animation = self.sprite_sheet[key]
            sprite_len = len(animation) - 1
            if self.num_sprites > sprite_len:
                self.flip = False
                self.num_sprites = 0

            if self.flip:
                # flip all textures
                for i in animation:
                    self.atlas[str(i)].flip_horizontal()
                # after that set flip to False to enable flip again
                self.flip = False
            self.image.texture = self.atlas[str(animation[self.num_sprites])]
            # self.canvas.clear()
            # with self.canvas:
            #     Rectangle(
            #         texture=self.atlas[str(animation[self.num_sprites])],
            #         pos=self.pos, size=self.size
            #     )

            if not self.pause_frame:
                self.num_sprites += 1

    def flip_h(self):
        self.flip = True
        self.num_sprites = 0

    def gravity_on(self, **kwargs):
        self.speed += self.gravity
        self.y -= self.speed
        if self.y < 42:
            self.jumps = 0
            self.y = 42

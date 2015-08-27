import kivy
from kivy.app import App
from kivy.atlas import Atlas
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from sprite import Sprite
from kivy.core.window import Window

__version__ = '0.1'

# Window.clearcolor = [1, 1, 1, 1]


class ScreenManagement(ScreenManager):
    pass


class GameView(Screen):
    tile_atlas = Atlas("imgs/tiles/tile.atlas")
    background_image = ObjectProperty(
        Image(source='imgs/forest8bit.jpg')
    )

    def __init__(self, **kwargs):
        super(GameView, self).__init__(**kwargs)
        self.ryu_atlas = Atlas("imgs/megaboy/mini.atlas")
        self.ryu_sheet = {"run": ["run_1", "run_2", "run_3", "run_4"]}
        self.sprite = Sprite(self.ryu_sheet, self.ryu_atlas)
        self.sprite.y = 500
        self.sprite.x = 100
        self.sprite.sprite_fps = 2
        self.add_widget(self.sprite)
        self.rigth = True
        self.back = False
        self.sprite.size_hint = [1.0 / x * 10 for x in self.sprite.size]
        print self.sprite.size, self.sprite.size_hint
        # must be int, not delta time
        self.fps = 0
        # self.sprite.flip = True

    def update(self, dt):
        self.fps += 1
        self.sprite.play("run", self.fps)
        self.sprite.gravity_on()
        self.walk_way()
        if self.fps > 30:
            self.fps = 0

    def walk_way(self):
        print self.sprite.x, self.width
        if self.sprite.x < self.width - self.sprite.width and self.rigth:
            self.sprite.x += 6
        else:
            if not self.back:
                self.back = True
                self.sprite.flip_h()

            self.rigth = False

        if self.sprite.x > self.width - self.width and not self.rigth:
            self.sprite.x += -6
        else:
            if self.back:
                self.back = False
                self.sprite.flip_h()
            self.rigth = True

    def jump(self):
        if self.sprite.jumps < 2:
            self.sprite.jumps += 1
            self.sprite.speed = -self.sprite.jump_force


class GameApp(App):
    def build(self):
        game_view = GameView()
        Clock.schedule_interval(game_view.update, 1 / 30.0)
        return game_view


if __name__ == "__main__":
    GameApp().run()

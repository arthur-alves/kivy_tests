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
    background_image = ObjectProperty(
        Image(source='imgs/forest8bit.jpg')
    )


class GameView(Screen):
    tile_atlas = Atlas("imgs/tiles/tile.atlas")
    background_image = ObjectProperty(
        Image(source='imgs/forest8bit.jpg')
    )

    def __init__(self, **kwargs):
        super(GameView, self).__init__(**kwargs)
        self.ryu_atlas = Atlas("imgs/ryu.atlas")
        self.ryu_sheet = {"run": ["ryu_1", "ryu_2", "ryu_3"]}
        self.sprite = Sprite(self.ryu_sheet, self.ryu_atlas)
        self.sprite.y = 500
        self.sprite.x = 100
        self.sprite.sprite_fps = 6
        self.add_widget(self.sprite)
        self.sprite.size_hint = [1.0 / x * 10 for x in self.sprite.size]
        print self.sprite.size, self.sprite.size_hint
        # must be int, not delta time
        self.fps = 0
        # self.sprite.flip = True

    def update(self, dt):
        self.fps += 1
        self.sprite.play("run", self.fps)
        self.sprite.gravity_on()
        if self.fps > 30:
            self.fps = 0

    def jump(self):
        if self.sprite.jumps < 2:
            self.sprite.jumps += 1
            self.sprite.speed = -self.sprite.jump_force


class GameApp(App):
    def build(self):
        game_view = GameView()
        Clock.schedule_interval(game_view.update, 1 / 60.0)
        return game_view


if __name__ == "__main__":
    GameApp().run()
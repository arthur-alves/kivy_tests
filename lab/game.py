from kivy.app import App
from kivy.atlas import Atlas
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from sprite import Sprite
from kivy.core.window import Window

Window.clearcolor = [1, 1, 1, 1]


class GameView(Screen):

    def __init__(self, **kwargs):
        super(GameView, self).__init__(**kwargs)
        self.ryu_atlas = Atlas("imgs/ryu.atlas")
        self.tile_atlas = Atlas("imgs/tiles/tile.atlas")
        self.ryu_sheet = {"run": ["ryu_1", "ryu_2", "ryu_3"]}
        self.sprite = Sprite(self.ryu_sheet, self.ryu_atlas)
        self.add_widget(self.sprite)
        self.sprite.size_hint = [1.0 / x * 10 for x in self.sprite.size]
        print self.sprite.size, self.sprite.size_hint
        # must be int, not delta time
        self.fps = 0
        # self.sprite.flip = True

    def update(self, dt):
        self.fps += 1
        self.sprite.play("run", self.fps)
        if self.fps > 30:
            self.fps = 0


class GameApp(App):
    def build(self):
        game_view = GameView()
        Clock.schedule_interval(game_view.update, 1 / 30.0)
        return game_view


if __name__ == "__main__":
    GameApp().run()

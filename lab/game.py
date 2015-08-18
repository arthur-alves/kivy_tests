from kivy.app import App
from kivy.atlas import Atlas
from kivy.uix.widget import Widget
from kivy.clock import Clock
from sprite import Sprite
from functools import partial


class GameView(Widget):

    def __init__(self, **kwargs):
        super(GameView, self).__init__(**kwargs)
        self.sprite = Sprite(sprite_sheet={"run": ["ryu_1", "ryu_2", "ryu_3" ]})
        self.add_widget(self.sprite)



class GameApp(App):
    def build(self):
        game_view = GameView()
        Clock.schedule_interval(partial(game_view.sprite.play, "run"), 0.2)
        return game_view


if __name__ == "__main__":
    GameApp().run()

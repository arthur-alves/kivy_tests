from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from sprite import Sprite
from functools import partial

Window.clearcolor = [0, 0, 0, 0]


class ScreenController(ScreenManager):
    pass


class MainScreen(Screen):
    sprite = Sprite(sprite_sheet={"walk": [0, 1, 2, 3]})
    # sprite = ObjectProperty(None)
    # sprite_id = 0

    # def anime(self, delta):
    #     if self.sprite_id > 3:
    #         self.sprite_id = 0
    #     self.sprite.source = "atlas://../piu/testatlas/{}".format(self.sprite_id)
    #     self.sprite_id += 1

    Clock.schedule_interval(partial(sprite.play, "walk"), 0.2)


class AnimeApp(App):
    def build(self):
        return ScreenController()


if __name__ == "__main__":
    global MAIN
    MAIN = AnimeApp
    MAIN().run()

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock

Window.clearcolor = [0, 0, 0, 0]


class ScreenController(ScreenManager):
    pass

class MainScreen(Screen):
    sprite = ObjectProperty(None)
    sprite_id = 0

    def anime(self, delta):
        if self.sprite_id > 3:
            self.sprite_id = 0
        self.sprite.source = "atlas://../piu/testatlas/{}".format(self.sprite_id)
        self.sprite_id += 1

    def update(self):
        Clock.schedule_interval(self.anime, 0.2)


class AnimeApp(App):
    def build(self):
        return ScreenController()


if __name__ == "__main__":
    global MAIN
    MAIN = AnimeApp
    MAIN().run()

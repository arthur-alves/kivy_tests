from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class ScreenController(ScreenManager):
    pass


class MainScreen(Screen):
    sprite = ObjectProperty(None)
    pass

class GameScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        return ScreenController()


if __name__ == "__main__":
    MainApp().run()
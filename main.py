import sqlite3
import time
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
import action
from kivy.resources import resource_add_path
import os
import sys
def resource_path(relative_path):
    """Retourne le chemin correct que ce soit en développement ou en fichier .exe (PyInstaller)"""
    try:
        # Si l'application tourne en tant qu'exécutable (PyInstaller)
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
    except Exception as e:
        pass
    # Si non, retourne simplement le chemin relatif
    return os.path.join(os.path.abspath("."), relative_path)
Builder.load_file(resource_path("action.kv"))
Builder.load_file(resource_path("list.kv"))
Builder.load_file(resource_path("show.kv"))
Builder.load_file(resource_path("myscreen.kv"))
Builder.load_file(resource_path("mainwidget.kv"))
Builder.load_file(resource_path("showed.kv"))




class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

class Screen2(Screen):
    pass
class MyScreen(ScreenManager):
    conn = sqlite3.connect(resource_path("friend.db"))
    """def __init__(self,**kwargs):
        super(MyScreen, self).__init__(**kwargs)
    def on_mouse_enter(self):
        Window.set_system_cursor('hand')"""


class FriendApp(App):
    manager = None

    def build(self):
        self.icon='icon.png'
        self.icon_size=(40,40)
        self.manager = MyScreen()
        return self.manager


if __name__=="__main__":
    FriendApp().run()


#app = App.get_running_app()
#my_manager = app.manager
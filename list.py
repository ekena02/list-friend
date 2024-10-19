from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class List(BoxLayout):
    def __init__(self,**kwargs):
        super(List, self).__init__(**kwargs)
        self.orientation='vertical'
        self.layout = BoxLayout(orientation='vertical')


    def ajouter(self, instance, *args):

        self.lbl = Label(text = instance)
        self.add_widget(self.lbl)

class Show(FloatLayout):
    def __init__(self,**kwargs):
            super(Show, self).__init__(**kwargs)

    def on_mouse_enter(self):
        Window.set_system_cursor('hand')
    def on_mouse_leave(self):
        Window.set_system_cursor("arrow")

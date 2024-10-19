from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)  # Couleur rouge
            self.ellipse = Ellipse(pos=(100, 100), size=(100, 100))  # Dessiner un cercle
            # Stocker les coordonnées et la taille de l'ellipse
            #self.ellipse_pos = (100, 100)
            #self.ellipse_size = (100, 100)

    def on_touch_down(self, touch):
        # Vérifiez si le toucher est dans le cercle
        if self.is_point_inside_ellipse(touch.pos):
            print("Le cercle a été touché!")

    def is_point_inside_ellipse(self, point):
        """Vérifie si un point est à l'intérieur de l'ellipse."""
        # Obtenez les coordonnées du point
        px, py = point
        # Obtenez les coordonnées et la taille de l'ellipse
        ex, ey = self.ellipse.pos
        ew, eh = self.ellipse.size
        # Convertir les coordonnées en coordonnées centrées
        px -= ex + ew / 2
        py -= ey + eh / 2
        # Vérifiez si le point est à l'intérieur de l'ellipse
        return (px ** 2) / (ew / 2) ** 2 + (py ** 2) / (eh / 2) ** 2 <= 1

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()


"""from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)  # Couleur rouge
            self.ellipse = Ellipse(pos=(100, 100), size=(100, 100))  # Dessiner un cercle

    def on_touch_down(self, touch):
        # Vérifiez si le toucher est dans le cercle
        if self.ellipse.collide_point(*touch.pos):
            print("Le cercle a été touché!")
        else:print("le cercle n'a pas été touché")

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()"""

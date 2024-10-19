import sqlite3

from kivy.app import App
from kivy.uix import popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


class MainShowed(BoxLayout):
    pass

class Showed(AnchorLayout):
    def __init__(self, **kwargs):
        super(Showed, self).__init__(**kwargs)
    def reinitialize_confirmation(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Do you really want to reset ?"))
        button = BoxLayout(orientation='horizontal')
        self.button_yes = Button(text="YES")
        self.button_yes.bind(on_press=self.reinitialize)
        self.button_no = Button(text="NO")
        self.button_no.bind(on_press=self.reinitialize)
        button.add_widget(self.button_yes)
        button.add_widget(self.button_no)
        content.add_widget(button)
        self.popup_confirmation=Popup(title='Confirmation', content=content, size_hint=(None, None), size=(300, 200))
        self.popup_confirmation.open()
    def reinitialize(self,instance):
        if instance==self.button_yes:
            self.popup_confirmation.dismiss()
            app = App.get_running_app()
            app.manager.ids.mainshowed.ids.showed.ids.list_added.ids.list_added_child.ids.list_added_child1.returne()
            app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1.returne1()
            app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1.labels.clear()
            app.manager.ids.mainshowed.ids.showed.ids.list_added.ids.list_added_child.ids.list_added_child1.labels.clear()
            #conn = sqlite3.connect("friend.db")
            conn = app.manager.conn
            c = conn.cursor()
            c.execute("DELETE FROM friends")

            c = conn.cursor()
            c.execute("DELETE FROM friends_removed")
            conn.commit()
            c.close()
            print("deleted successfully")


            app.manager.transition.direction='right'
            app.manager.current='MainWidget'
            Popup(title='reset', content=Label(text='reset successfully'), size_hint=(None, None), size=(300,200)).open()
        else:
            self.popup_confirmation.dismiss()



class ListAddedChild(BoxLayout):
    def __init__(self, **kwargs):
        super(ListAddedChild, self).__init__(**kwargs)
        self.orientation = 'vertical'
        conn = sqlite3.connect("friend.db")
        #conn = App.get_running_app().manager.conn
        c = conn.cursor()
        c.execute("SELECT * FROM friends")
        friends = c.fetchall()
        conn.commit()
        conn.close()
        self.labels = [] #les données globales de la liste
        self.lbls=[] #les données temporaires pour afficher
        for friend in friends:
            self.labels.append(friend[1])
    def adde(self,text):
        self.labels.append(text)
        print(text, "added")
        app=App.get_running_app()
        #app.manager.ids.mainshowed.ids.showed.ids.list_added.ids.list_removed_child.remove(text)
        listremovedchild = app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1
        list_removed = listremovedchild.labels
        if text in list_removed:
            list_removed.remove(text)
            #conn = sqlite3.connect("friend.db")
            conn = App.get_running_app().manager.conn
            c=conn.cursor()
            c.execute("DELETE FROM friends_removed WHERE name=?",(text,))
            conn.commit()
            conn.close()
    def removee(self, text):
        if text in self.labels:
            self.labels.remove(text)
            #app = App.get_running_app()
            #app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.remove(text)

    def showall(self):
        print("debogage dans showall")
        app = App.get_running_app()
        app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1.showall1()
        for friend in sorted(self.labels):
            self.lbls.append(Label(text=f'[b]{friend}[/b]',markup=True,size_hint=(1,None),height=50))
        for lbl in self.lbls:
            self.add_widget(lbl)
            #self.remove_widget(lbl)
    def returne(self):
        print("return successfully")
        for lbl in self.lbls:
            self.remove_widget(lbl)
        self.lbls.clear()
        #self.labels.clear()
        app=App.get_running_app()
        app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1.returne1()




       #while not self.lbls[-1]==None
        #    dele = self.lbls[-1]
         #   self.remove_widget(dele)
          #  self.lbls.pop()
        #else:pass
        #"""





class ListRemovedChild(BoxLayout):
    def __init__(self, **kwargs):
        super(ListRemovedChild, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.labels = [] #données globales de la liste
        self.lbls = [] # données temporaires pour afficher les listes
        conn=sqlite3.connect("friend.db")
        #conn = App.get_running_app().manager.conn
        c=conn.cursor()
        friends_removed=c.execute("SELECT * FROM friends_removed").fetchall()
        for friend_removed in friends_removed:
            self.labels.append(friend_removed[1])
    def remove(self,text):
        self.labels.append(text)
    def showall1(self):
        for friend in sorted(self.labels):
            self.lbls.append(Label(text=f'[b]{friend}[/b]',markup=True,size_hint=(1,None),height=50))
        for lbl in self.lbls:
            self.add_widget(lbl)
    def returne1(self):
        for lbl in self.lbls:
            self.remove_widget(lbl)
        self.lbls.clear()
        #self.labels.clear()





import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Action(BoxLayout):
    pass


class ActionAdd(BoxLayout):
    def add(self):   #ici, on l'enregistre juste dans la db et il appelera la donction qui ajoute dans liste
        text = self.ids._friend_add.text.title()
        if not text == '':
            app = App.get_running_app()
            #self.parent.parent.ids.list_widget.ajouter(text)
            self.ids._friend_add.text = ""
            self.ids._friend_add.hint_text = "add..."
            #conn = app.manager.conn
            conn = sqlite3.connect("friend.db")
            c = conn.cursor()
            c.execute("""
                        CREATE TABLE IF NOT EXISTS friends (
                        id INTEGER PRIMARY KEY, name TEXT )
                    """)
            for friend in c.execute("SELECT * FROM friends").fetchall():
                if friend[1] == text:
                    print("friend already exist")
                    Popup(title='IMPOSSIBLE', content=Label(text='friend already exist'), size_hint=(None, None),
                          size=(300, 200)).open()
                    conn.commit()
                    conn.close()

                    return 0
            else:
                c.execute("INSERT INTO friends (name) VALUES (?)", (text,))
                #print(text, "added")
            #c.execute("SELECT * FROM friends")
            #friends = c.fetchall()

            conn.commit()
            conn.close()
            #for friend in friends:
            #   print(friend[1])

            App.get_running_app().manager.ids.mainshowed.ids.showed.ids.list_added.ids.list_added_child.ids.list_added_child1.adde(text)
            print(True)
        else:
            print("cannot add an empty name")
            Popup(title='IMPOSSIBLE', content=Label(text='Cannot add an empty name'), size_hint=(None, None),
                  size=(300, 200)).open()



class ActionRemove(BoxLayout):
    def remove(self):
        text = self.ids._friend_remove.text.title()
        if not text == '':
            print(type(self.ids._friend_remove))
            self.ids._friend_remove.text = ''
            self.ids._friend_remove.hint_text = 'rem...'
            #conn = App.get_running_app().manager.conn
            conn = sqlite3.connect("friend.db")
            c = conn.cursor()
            friends = c.execute("SELECT * FROM friends").fetchall()
            for friend in friends:  #voir si friend est dans la base de données pour pouvoir la supprimer
                if text == friend[1]:
                    print(text, "removed")
                    App.get_running_app().manager.ids.mainshowed.ids.showed.ids.list_added.ids.list_added_child.ids.list_added_child1.removee(
                        text)
                    c.execute("DELETE FROM friends WHERE (name) =(?)", (text,))
                    conn.commit()
                    conn.close()
                    conn = sqlite3.connect("friend.db")
                    c = conn.cursor()
                    c.execute("""
                                CREATE TABLE IF NOT EXISTS friends_removed(id INTEGER PRIMARY KEY, name TEXT)
                                """)
                    #inserer dans la base ssi elle n'y existe pas encore
                    ifexist=c.execute("SELECT * FROM friends_removed WHERE name=?", (text,)).fetchall()
                    print(ifexist)
                    if ifexist==[]:
                        c.execute("INSERT INTO friends_removed(name) VALUES(?)", (text,))
                    conn.commit()
                    conn.close()
                    app=App.get_running_app()
                    app.manager.ids.mainshowed.ids.showed.ids.list_removed.ids.list_removed_child.ids.list_removed_child1.remove(text)
                    return
            else:
                print("cannot remove a friend who does not exist")
                Popup(title='IMPOSSIBLE', content=Label(text='Cannot remove a friend who does not exist'), size_hint=(None, None),
                      size=(360, 200)).open()
            conn.commit()
            conn.close()
        else:
            print("cannot remove an empty text")
            Popup(title='IMPOSSIBLE', content=Label(text='cannot remove an empty text'),
                  size_hint=(None, None),
                  size=(300, 200)).open()



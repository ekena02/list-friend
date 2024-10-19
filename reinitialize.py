import sqlite3

from kivy.app import App


def reinitializee():
    #conn = sqlite3.connect("friend.db")
    conn = App.get_running_app().manager.conn
    c = conn.cursor()
    c.execute("DELETE FROM friends")

    c = conn.cursor()
    c.execute("DELETE FROM friends_removed")
    conn.commit()
    c.close()
    print("deleted successfully")
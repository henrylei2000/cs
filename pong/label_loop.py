from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.button import Button
import time
import threading

class Test(GridLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.cols = 2
        self.thislabel1 = Label(text="One")
        self.add_widget(self.thislabel1)
        self.thislabel2 = Label(text="Two")
        self.add_widget(self.thislabel2)
        self.thislabel3 = Label(text="Three")
        self.add_widget(self.thislabel3)
        self.thislabel4 = Label(text="Four")
        self.add_widget(self.thislabel4)
        self.thislabel5 = Label(text='Five')
        self.add_widget(self.thislabel5)
        self.button1 = Button(text='Shrink Ray')
        self.button1.bind(on_release=self.shrinkstart)  # here the button targets the thread starter function
        self.add_widget(self.button1)
        self.these_children = [self.thislabel1,self.thislabel2,self.thislabel3,self.thislabel4,self.thislabel5]

    def shrinkstart(self, *args):
        t = threading.Thread(target=self.shrinkray)  # initiate the thread
        t.daemon = True  # daemon thread so it terminates when stopping the main thread
        t.start()

    def shrinkray(self):
        anim = Animation(font_size=1)
        for these_labels in self.these_children:
            anim.start(these_labels)
            time.sleep(1.5)


class MyApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    MyApp().run()
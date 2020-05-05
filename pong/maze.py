from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.config import Config
from kivy.graphics import Line, Color, Rectangle, Ellipse, Rotate
from kivy.animation import Animation
import time
import threading
from random import random as r

class results(Screen):
    reset = NumericProperty(0)
    anim_pt = ListProperty([])    # this is the line endpoint
    ss = ListProperty([])

    def on_enter(self):
        self.start_daemon()

    def start_daemon(self, *args):
        t = threading.Thread(target=self.draw)  # initiate the thread
        t.daemon = True  # daemon thread so it terminates when stopping the main thread
        t.start()

    def draw(self):
        p1 = [100, 100]
        p2 = [200, 400]
        p3 = [400, 400]
        p4 = [300, 100]
        points = [p1, p2, p4]

        with self.canvas:
            Color(r(), 1, 1, mode='hsv')
            Line(points=p1 + p2 + p4 + p1, width=2)

        self.patternize(points, 0.1)

        with self.canvas:
            self.rot = Rotate()
            self.rot.axis = (0, 0, 1)
            self.rot.origin = self.center
            self.rot.angle = 10
            Line(ellipse=(400, 440, 200, 100, 0, 360), width=2)
            Line(ellipse=(400, 440, 190, 90, 0, 360), width=2)

    def patternize(self, points, pace):
        for i in range(10):
            # [[x, y], [x, y], [x, y], [x, y]]

            if self.too_close(points):
                break

            px = points[0][0]  # avoid side effect on p1 list
            py = points[0][1]  # avoid side effect on p1 list
            collector = []

            number_of_points = len(points)

            for k in range(number_of_points):
                if k < number_of_points - 1:
                    x = int(points[k][0] + (points[k+1][0] - points[k][0]) * pace)
                    y = int(points[k][1] + (points[k+1][1] - points[k][1]) * pace)
                else:
                    x = int(points[k][0] + (px - points[k][0]) * pace)
                    y = int(points[k][1] + (py - points[k][1]) * pace)

                points[k] = [x, y]
                collector.append(points[k])

            collector.append(points[0])

            for j in range(len(collector) - 1):
                self.ss.clear()
                self.anim_pt = collector[j]
                self.ss = collector[j]
                anim = Animation(anim_pt=collector[j + 1], d=1)
                anim.start(self)
                time.sleep(1)
                anim.stop(self)

        self.ss.clear()

    def too_close(self, points):
        if len(points) < 2:
            return True
        else:
            if (points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2 < 100:
                return True
        return False

    def on_anim_pt(self, widget, progress):
        # called when anim_pt changes

        # set up the line points
        points = self.ss
        points.extend(self.anim_pt)

        # draw the updated line
        with self.canvas:
            Color(r(), 1, 1, mode='hsv')
            self.line = Line(points=points, width=2)


class mazeupdateApp(App):
    Config.set('graphics', 'width', '1920')
    Config.set('graphics', 'height', '1080')

    def build(self):
        FadeTransition.clearcolor = (1,1,1,1)
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(results(name='one'))
        return sm


if __name__ == '__main__':
    mazeupdateApp().run()
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.config import Config
from kivy.graphics import Line, Color, Rectangle, Ellipse, Rotate
from kivy.animation import Animation
import time
import threading
from random import random as r
from math import *

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

        c = (960, 540)  # center
        half_w = 40

        ngon = 12
        # sun = self.draw_ngon(ngon, 290, c)
        triangles = self.draw_triangle(12, 250, c)
        for i in range(len(triangles)):
            self.patternize(triangles[i], 0.1)

        # self.patternize(sun, 0.5)

    def draw_ngon(self, n, radius, position):
        pi2 = 2 * 3.14
        points = []
        for i in range(n):
            points.append([cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]])

        return points

    def draw_triangle(self, n, radius, position):
        pi2 = 2 * 3.14
        points = []
        inner_triangles = []
        for i in range(n):
            points.append([cos((i + .5)/ n * pi2) * radius + position[0], sin((i + .5) / n * pi2) * radius + position[1]])

        for i in range(n):
            if i < n - 1:
                inner_triangles.append([points[i], points[i + 1], position])
            else:
                inner_triangles.append([points[i], points[0], position])

        r = radius + 250
        triangles = []
        for i in range(n):
            top = [cos((i + 1) / n * pi2) * r + position[0], sin((i+1) / n * pi2) * r + position[1]]
            if i < n - 1:
                triangles.append([points[i], points[i+1], top])
            else:
                triangles.append([points[i], points[0], top])

        all_points = []
        for i in range(n):
            all_points.append(inner_triangles[i])
            all_points.append(triangles[i])

        return all_points

    def mirror(self, points, center, direction="h"):
        mirror_side = []
        for p in points:
            if direction == "h":  # horizontal flip
                mp = self.mirror_x(p, center)
            else:
                mp = self.mirror_y(p, center)
            mirror_side.append(mp)

        mirror_side.reverse()
        return mirror_side

    def mirror_x(self, point, center):
        mirror = [point[0], point[1]]
        mirror[0] += (center - point[0]) * 2  # gap
        return mirror

    def mirror_y(self, point, center):
        mirror = [point[0], point[1]]
        mirror[1] -= (point[1] - center) * 2  # gap
        return mirror

    def patternize(self, points, pace):

        with self.canvas:
            Color(.1, .1, .9)
            Line(points=(points+[points[0]]), width=2)

        for i in range(50):
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
                anim = Animation(anim_pt=collector[j + 1], d=.2)
                anim.start(self)
                time.sleep(.3)
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
            Color(.9, .9, .9)
            self.line = Line(points=points, width=1)


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
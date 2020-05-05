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
    color = NumericProperty(0)
    anim_pt = ListProperty([])    # this is the line endpoint
    ss = ListProperty([])

    def on_enter(self):
        self.start_daemon()

    def start_daemon(self, *args):
        self.color = 0.65
        t = threading.Thread(target=self.draw)  # initiate the thread
        t.daemon = True  # daemon thread so it terminates when stopping the main thread
        t.start()

    def draw(self):
        bottom = 130
        p1 = [2, 130]
        p2 = [42, 130]
        p3 = [42, 160]
        p4 = [12, 170]
        p5 = [42, 175]
        p6 = [22, 190]
        p7 = [90, 205]
        p8 = [130, 230]
        p9 = [130, 222]

        center = [180, 222]
        points = [p1]
        left_side = [p2, p3, p4, p5, p6, p7, p8, p9]
        points += left_side
        points.append(center)
        right_side = self.mirror(left_side, center[0])
        points += right_side

        c1 = [[336, 130], [336, 144], [368, 144]]
        points += c1
        left2 = [[368, 164], [378, 164], [378, 204]]
        points += left2
        c2 = [400, 208]
        points.append(c2)
        right2 = self.mirror(left2, c2[0])
        points += right2

        base = points[len(points) - 1]
        x, y = base[0], base[1]

        b3 = [[x, y - 10], [x + 12, y - 10], [x + 12, y + 150], [x + 30, y + 160], [x + 65, y + 148], [x + 65, y + 20],
              [x + 70, y + 20], [x + 70, bottom], [x + 85, bottom], [x + 85, bottom + 130], [x + 135, bottom + 140],
              [x + 155, bottom + 128], [x + 155, y], [x + 170, y - 5], [x + 170, y - 15], [x + 185, y - 15],
              [x + 185, y - 5], [x + 185, y + 15], [x + 210, y + 25], [x + 235, y + 15], [x + 235, bottom]]
        points += b3
        x, y = x + 235, bottom
        b4 = [[x + 15, y], [x+20, y+25], [x+70, y+25], [x+72, y+32], [x+112, y+32], [x+115, y+38], [x+155, y+38],
              [x+170, y+95], [x+167, y+97], [x+172, y+100], [x+164, y+110], [x+190, y+113], [x+175, y+125],
              [x+197, y+130], [x+227, y+150], [x+227, y+160], [x+227, y+161]]
        points += b4
        c3 = [x + 232, y + 162]
        points.append(c3)
        b4r = self.mirror(b4, c3[0])
        points += b4r

        base = points[len(points) - 1]
        x, y = base[0], base[1]
        b5 = [[x+15, y], [x+15, y+80], [x+35, y+140], [x+55, y+80], [x+55, y+20], [x+85, y+20], [x+85, y+8],
              [x+100, y]]
        points += b5

        b6 = [[x+100, y+35], [x+115, y+35], [x+125, y+40], [x+145, y+45]]
        points += b6
        c6 = [x+146, y+45]
        points.append(c6)
        b6r = self.mirror(b6, c6[0])
        points += b6r

        base = points[len(points) - 1]
        x, y = base[0], base[1]
        b7 = [[x, y-15], [x+15, y-15], [x+15, y-30], [x+30, y-30], [x+30, y+80], [x+50, y+90], [x+90, y+75],
              [x+90, y+30], [x+97, y+25], [x+97, y-20], [x+111, y-20], [x+111, y+120], [x+151, y+130], [x+165, y+120],
              [x+165, y+10], [x+172, y+7], [x+172, bottom], [x+190, bottom], [x+192, bottom + 2]]
        points += b7

        base = points[len(points) - 1]
        x, y = base[0], base[1]

        # 101
        b8 = [[x+20, y], [x+30, y+60], [x+26, y+90], [x+30, y+90], [x+26, y+125], [x+30, y+125], [x+26, y+160],
              [x+30, y+160], [x+26, y+190], [x+30, y+190], [x+26, y+220], [x+30, y+220], [x+26, y+255], [x+30, y+255],
              [x+26, y+290], [x+30, y+290], [x+45, y+310], [x+45, y+340], [x+47, y+342], [x+47, y+357], [x+49, y+380]]
        points += b8

        c8 = [x + 50, y + 400]
        points.append(c8)
        b8r = self.mirror(b8, c8[0])
        points += b8r

        base = points[len(points) - 1]
        x, y = base[0], base[1]

        b9 = [[x+15, y], [x+15, y+2], [x+30, y+2], [x+30, y+30], [x+55, y+30], [x+70, y+45], [x+85, y+30],
              [x+110, y+30], [x+110, bottom]]
        points += b9

        self.patternize(points, 0, False)

        self.color = 0.1
        self.patternize(points, 0, False)

    def mirror(self, points, center):
        mirror_side = []
        for p in points:
            mp = self.mirror_x(p, center)
            mirror_side.append(mp)

        mirror_side.reverse()
        return mirror_side

    def mirror_x(self, point, center):
        mirror = [point[0], point[1]]
        mirror[0] += (center - point[0]) * 2  # gap
        return mirror

    def patternize(self, points, pace, closed=True):
        for i in range(1):
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
            if closed:
                collector.append(points[0])

            for j in range(len(collector) - 1):
                self.ss.clear()
                self.anim_pt = collector[j]
                self.ss = collector[j]
                anim = Animation(anim_pt=collector[j + 1], d=0.55)
                anim.start(self)
                time.sleep(.6)
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
            Color(self.color, .6, .6)
            Color(r(), r(), r())
            self.line = Line(points=points, width=4)


class mazeupdateApp(App):
    Config.set('graphics', 'width', '1920')
    Config.set('graphics', 'height', '1080')

    def build(self):
        from kivy.core.window import Window
        Window.clearcolor = (.8, .8, .7, .9)
        sm = ScreenManager()
        sm.add_widget(results(name='one'))
        return sm


if __name__ == '__main__':
    mazeupdateApp().run()
from __future__ import print_function

__author__ = 'sjosund'


from abc import abstractmethod
from threading import Timer
from time import sleep
from Xlib import display


class Subject(object):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        """
        :type observer: Observer
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        :type observer: Observer
        """
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.data())

    @abstractmethod
    def data(self):
        pass


class MousePositionSubject(Subject):
    def __init__(self):
        super(MousePositionSubject, self).__init__()
        self.last_position = MousePositionSubject.mouse_position()

    def run(self):
        while True:
            self._update()
            sleep(0.001)
            # t = Timer(0.01, self._update)
            # t.start()

    def _update(self):
        current_position = MousePositionSubject.mouse_position()
        if current_position != self.last_position:
            self.last_position = current_position
            self.notify()

    def data(self):
        return MousePositionSubject.mouse_position()

    @staticmethod
    def mouse_position():
        d = display.Display().screen().root.query_pointer()._data  # Clean code comment about this?
        p = Point(d['root_x'], d['root_y'])
        return p


class MousePositionObserver(object):
    def __init__(self, name):
        self.position = Point(0, 0)
        self.name = name

    def update(self, position):
        self.position = position
        self.display()

    def display(self):
        print("{} - {}".format(self.name, self.position))


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "x = {}, y = {}".format(self.x, self.y)


if __name__ == "__main__":
    o1 = MousePositionObserver('o1')
    o2 = MousePositionObserver('o2')
    s = MousePositionSubject()
    s.register_observer(o1)
    s.register_observer(o2)
    s.run()

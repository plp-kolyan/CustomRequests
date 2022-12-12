import threading

from src.requestsgarant import *
from unittest import TestCase


class TestTestCase(TestCase):
    def test_0(self):
        class Flag:
            def __init__(self):
                self.succses = True

            def f(self):
                self.f = True

        print(Flag().__dict__)
        f = Flag()
        f.f()
        print(f.__dict__.keys())


        for attr in [attr for attr in f.__dict__.keys()]:
            args = (f, attr)
            if hasattr(*args):
                delattr(*args)

        print(f.__init__())
        print(f.__dict__)

    def test_1(self):
        def u(*args):
            for i in args:
                print(i)

            return u(*args)
        u(1,1,3)

    def test_2(self):
        import queue
        startqueue = queue.Queue()
        endqueue = queue.Queue()

        for n in range(1000):
            startqueue.put(n)

        def f():
            while True:
                endqueue.put(startqueue.get())
                startqueue.task_done()

        def pp():
            while endqueue.get_nowait:
                print(endqueue.get())
                endqueue.task_done()


        
        threading.Thread(target=f, daemon=True).start()
        threading.Thread(target=pp, daemon=True).start()
        startqueue.join()
        endqueue.join()




class UpdateTomlTestCase(TestCase):
    def test_open(self):
        with open('pyproject.toml', 'r') as file:
            print(file.read())

    def up_version(self, version_list, index=None):
        if index is None:
            last_index = len(version_list) - 1
        else:
            last_index = index
        version_list[last_index] = str(int(version_list[last_index]) + 1)

        if last_index == 0:
            return '.'.join(version_list)
        else:
            if last_chr := int(version_list[last_index]) > 9:
                version_list[last_index] = str(last_chr // 10)
                last_index -= 1
                return self.up_version(version_list, last_index)
            return '.'.join(version_list)

    def test_open_toml(self):
        import toml
        data = {}

        with open("pyproject.toml", "r") as file:
            data = toml.load(file)
            version_list = data['project']['version'].split('.')
            data['project']['version'] = self.up_version(version_list)

        with open("pyproject.toml", "w") as file:
            toml.dump(data, file)


import threading

from src import requestsgarant
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





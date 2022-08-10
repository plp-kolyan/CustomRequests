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

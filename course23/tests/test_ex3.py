import unittest
import time


def foo(x):
    return 8 / x


def baz():
    return int(time.time()) % 60


def qux():
    current_second = baz()
    b_value = foo(current_second)
    return b_value


class TestSome(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(4), 2)
        self.assertEqual(foo(2), 4)

    def test_baz(self):
        self.assertGreaterEqual(baz(), 0)
        self.assertLess(baz(), 60)

    def test_qux(self):
        self.assertGreater(qux(), 0)
        self.assertLess(qux(), 8)



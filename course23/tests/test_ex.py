import unittest


# def div(x):
#     return 1 / (x - 1)

class TestStringMethods(unittest.TestCase):

    # def test_div(self):
    #     self.assertEqual(div(2), 1)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            # v = 1 / 0
            s.split(2)
            # s.split(' ')


if __name__ == '__main__':
    unittest.main()

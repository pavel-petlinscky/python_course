# -*- coding: utf-8 -*-

class AttributesClass(object):
    def __init__(self, values):
        # self.values = values
        super(AttributesClass, self).__setattr__('values', values)

    def __getattr__(self, item):
        return self.values[item]

    def __setattr__(self, key, value):
        self.values[key] = value


if __name__ == '__main__':
    v = {'one': 1, 'two': 2}
    # v['one']
    # v.one
    attr = AttributesClass({'one': 1, 'two': 2})
    attr.three = 3
    print(attr.three, attr.one)

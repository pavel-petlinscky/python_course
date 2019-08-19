#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Without args
p = lambda: print('Hey')
p()

ten = lambda x: 10
print(ten(9))

# With positional elements
n = lambda x, y: x + y
print(n(3, 4))

# we can use args
l = lambda *args: print(args)
l(list(range(1, 10)))

# we can use kwargs
kw_lambda = lambda **kwargs: print(kwargs)
kw_lambda(**{'a': 1, 'b': 2})
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LoD:
    """
    The law is simply this. In any piece of code, the code can only refer to:

    * Methods of self / this
    * Attributes of self / this
    * Methods of attributes of self / this. (This is the only case of using two 'dot's.)
    * Parameters to the method.
    * Methods of those parameters.
    * Stuff created as part of the method.
    * Methods of stuff created.
    """

    def OK(self):
        self.foo()
        self.a
        self.a.foo()
        bar.foo()
        baz = Baz()
        baz.foo()

    def BAD(self):
        self.foo().bar()
        self.foo().attr
        self.a.foo().attr
        self.a.foo().foo()
        bar.attr
        bar.foo().foo()
        bar.foo().attr
        baz = Baz()  # this is actually OK
        baz.attr
        baz.foo().attr
        baz.foo().foo()
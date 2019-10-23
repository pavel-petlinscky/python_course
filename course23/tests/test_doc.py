def run_once(f):
    """
    >>> @run_once
    ... def foo(n): return n + 1

    >>> foo(7)
    8

    >>> foo(0)
    8
    """
    def _f(*args, **kwargs):
        if not hasattr(_f, "_retval"):
            _f._retval = f(*args, **kwargs)
        return _f._retval
    return _f


if __name__ == "__main__":
    import doctest
    doctest.testmod()

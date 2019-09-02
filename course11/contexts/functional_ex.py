from contextlib import contextmanager


class CtxManager:
    def __enter__(self):
        print('some work before, __enter__')
        return 35

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print('Some exit wotr')


with CtxManager():
    #raise RuntimeError('35')
    print(7)







@contextmanager
def do_work(value):
    print('some work before, __enter__')
    yield value
    print('some work after, __exit__')
    yield 5


with do_work(14) as w:
    print('Some work here!')
    print(w)







@contextmanager
def open_some_file(filename, mode = 'r'):
    try:
        fd = open(filename, mode)
    except Exception as e:
        fd = None

    print('some work before, __enter__')
    yield fd
    if fd is not None:
        fd.close()
    print('some work after, __exit__')


with open_some_file('doesnotexist') as f:
    print('SOME WORK HERE')
    if f is not None:
        f.write('some data123')
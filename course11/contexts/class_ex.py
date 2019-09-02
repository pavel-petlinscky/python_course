class File(object):
    def __init__(self, filename, mode):
        print('__init__')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('opening file')
        try:
            self.open_file = open(self.filename, self.mode)
        except Exception as e:
            print("Exception in context manager")
            self.open_file = None

        return self.open_file

    def __exit__(self, *args):
        print('closing file')
        if self.open_file is not None:
            self.open_file.close()


#
with File('to_open.txt', 'w') as f:
    print('SOME WORK HERE')
    f.write('some data')

# Note how error is handled:

# with File('does-not-exist', 'r') as new_file:
#     if new_file is not None:
#         print(new_file.read())
















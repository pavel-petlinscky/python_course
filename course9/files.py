
def read_file(filename):
    print('reading file with read_file()')
    content = None
    try:
        f = open(filename)  # Unix-way - some_dir/file_name.txt, Windows-way - some_folder\file_name.txt
        try:
            content = f.read()
        finally:
            f.close()

    except FileNotFoundError:
        print('File not found')

    return content



def way_better(filename):
    print('reading file with way_better()')
    try:
        with open(filename) as f:
            return f.read()

    except FileNotFoundError:
        print('File not found')


def write_to_file(filename, content, mode='w'):

    with open(filename, mode=mode) as f:
    #with open(filename, mode='r') as f:
        f.write(content)

class Car:
    def __init__(self, color="red"):
        self.color=color

    def change_color(self, new_color):
        self.color = new_color

if __name__ == '__main__':
    print(way_better('/Users/ppetlinsky/workspace/tceh/python_course/course9/1.txt'))
    print(way_better('../1.txt'))
    # Reading:
    #print(read_file('toread.txt'))
    #print(way_better('toread.txt'))

    # Writing:
    write_to_file('new.txt', 'Some\ntext!')  # rewrites
    #write_to_file('new.txt', 'Some\ntext!')  # rewrites
    write_to_file('existing.txt', 'New line\n', mode='a')  # adds


















def read_file(filename):
    print('reading file with read_file()')
    content = None
    try:
        f = open(filename)  # Unix-way - some_dir/file_name.txt, Windows-way - sime_folder\file_name.txt
        try:
            content = f.read()
        finally:
            f.close()
    except Exception as e:
        print('problem while open file {}'.format(e))

    return content

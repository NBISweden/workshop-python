
import os

file_counter = 0

def print_dir(path='.',tab=0,min_size=0):
    global file_counter
    tab_level = '  ' * tab
    items = os.scandir(path)
    for item in items:
        if item.name.startswith('.'):
            continue
        if item.is_file():
            s = item.stat()
            size = humanize(s.st_size)
            name = item.path
            if s.st_size > min_size:
                print('{tab}|- {:>10} : {}'.format(size,name,tab=tab_level))
                file_counter += 1
        elif item.is_dir():
            if item.name.startswith('_'):
                #print('{0:*>10} {0} is a directory that I ignore'.format(item.name))
                pass
            else:
                print('{tab}Printing files from {}'.format(item.path,tab=tab_level))
                print_dir(item.path,tab = tab+1,min_size=min_size)
        else:
            print(item.name, ' is ignored')


SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def humanize(size):
    '''Converts a file size to human-readable form.'''

    if size < 0:
        raise ValueError('Size must be non-negative')

    if size < 1000:
        return '{0!s} B'.format(size)

    for suffix in SUFFIXES:
        size /= 1000
        if size < 1000:
            return '{0:.1f} {1}'.format(size, suffix)


    raise ValueError('Size too large')



import sys
main_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
min_size = int(sys.argv[2]) if len(sys.argv) > 2 else 0
print_dir(path=main_dir,min_size=min_size)
print(file_counter, ' files found in ',main_dir, ' larger than ', humanize(min_size))

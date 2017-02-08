from os import scandir as get_dir


def print_file_tree(path):
    """ Print the tree structure
        But does not recurse"""

    items = get_dir(path)
    for item in items:
        if item.name.startswith('.'):
            continue
        
        if item.is_file():
            print('FILE: ', item.path)
        elif item.is_dir():
            if item.name.startswith('_'):
                pass
            else:
                print('DIR: ', item.path)
        else:
            print(item.name, ' is ignored')
            


print_file_tree('.')


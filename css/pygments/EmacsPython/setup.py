""" 
My Emacs-Python style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'ep', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Frederic Haziza", 
    install_requires = ['pygments'],
    packages     = ['ep'],
    entry_points = '''
    [pygments.styles]
    EmacsPython = ep.ep:EPStyle
    '''
) 

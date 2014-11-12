from distutils.core import setup

setup(name='kao_project',
      version='.1',
      #description='Kao Tessur Deck Package',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_project',
                     'kao_project.commands',
                     'kao_project.extension'],
      scripts=['kao_project/scripts/kproj']
     )
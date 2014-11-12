from extension import Extension

import os
import subprocess

class PyLibExtension:
    """ Represents a Python Library """
    
    def onChange(self, parent):
        """ Install the library """
        os.chdir(parent.filepath)
        subprocess.call('python setup.py install')
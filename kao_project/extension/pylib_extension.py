from .extension import Extension

import os
import subprocess

class PyLibExtension(Extension):
    """ Represents a Python Library """
    
    def onChange(self, parent):
        """ Install the library """
        os.chdir(parent.srcpath)
        subprocess.call(['python', 'setup.py', 'install'])
import os
import subprocess

class GitExtension:
    """ Represents the git info of a project """
    
    def __init__(self):
        """ Initialize the Git Extension """
        
    def update(self, parent):
        """ Update the git project """
        os.chdir(parent.filepath)
        subprocess.call(['git', 'pull'])
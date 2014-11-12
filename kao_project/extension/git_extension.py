import os
import subprocess

class GitExtension:
    """ Represents the git info of a project """
    
    def __init__(self, url):
        """ Initialize the Git Extension """
        self.url = url
        
    def initialize(self, parent):
        """ Create the git connection """
        os.mkdir(parent.filepath)
        os.chdir(parent.filepath)
        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'remote', 'add', 'origin', self.url])
        subprocess.call(['git', 'pull', 'origin', 'master'])
        subprocess.call(['git', 'push', '-u', 'origin', 'master'])
        
    def update(self, parent):
        """ Update the git project """
        os.chdir(parent.filepath)
        subprocess.call(['git', 'pull'])
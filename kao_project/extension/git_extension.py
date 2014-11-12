import os
import subprocess

class GitExtension:
    """ Represents the git info of a project """
    NO_NEW_DATA = "Already up-to-date."
    
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
        process = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return process.returncode == 0 and self.NO_NEW_DATA != output.strip()
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
        pulledData = self.pull(['git', 'pull', 'origin', 'master'])
        subprocess.call(['git', 'push', '-u', 'origin', 'master'])
        return pulledData
        
    def update(self, parent):
        """ Update the git project """
        os.chdir(parent.filepath)
        return self.pull(['git', 'pull'])
        
    def onChange(self, parent):
        """ Do nothing when the project has changed """
        pass
        
    def pull(self, command):
        """ Pull from the origin """
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return process.returncode == 0 and self.NO_NEW_DATA != output.strip()
        
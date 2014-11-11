
class Project:
    """ Represents a project """
    
    def __init__(self, name, path):
        """ Initialize the project with its name and the path to its location on the file system """
        self.name = name
        self.path = path
        
    @property
    def goToAlias(self):
        """ Return the text for the alias command to go to this project """
        return 'alias a-{0}="cd {1}"'.format(self.commandName, self.path.filepath)
        
    @property
    def commandName(self):
        """ Return the command name for the project """
        return self.name.lower().replace(' ', '-')
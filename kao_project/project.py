
class Project:
    """ Represents a project """
    
    def __init__(self, name, path, extensions=[]):
        """ Initialize the project with its name and the path to its location on the file system """
        self.name = name
        self.path = path
        self.extensions = extensions
        
    @property
    def commandName(self):
        """ Return the command name for the project """
        return self.name.lower().replace(' ', '-')
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return self.path.filepath
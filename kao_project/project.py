import os

class Project:
    """ Represents a project """
    
    def __init__(self, name, path, extensions=[]):
        """ Initialize the project with its name and the path to its location on the file system """
        self.name = name
        self.path = path
        self.extensions = extensions
        
    def existsLocally(self):
        """ Return if the project exists locally """
        return os.path.exists(self.filepath)
        
    def install(self):
        """ Install the project """
        if any([extension.install(self) for extension in self.extensions]):
            self.onChange()
        
    def update(self):
        """ Update the project """
        if any([extension.update(self) for extension in self.extensions]):
            self.onChange()
                
    def onChange(self):
        """ Call on change for each extension """
        for extension in self.extensions:
            extension.onChange(self)
        
    @property
    def commandName(self):
        """ Return the command name for the project """
        return self.name.lower().replace(' ', '-')
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return self.path.filepath
        
    @property
    def srcpath(self):
        """ Return the source file path """
        return self.path.srcpath
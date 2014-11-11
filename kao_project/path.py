import os

class Path:
    """ Represents a path to a project """
    
    def __init__(self, envVar, pathFromEnvVar):
        """ Initialize the path """
        self.envVar = envVar # An Environment Variable containing a directory the Project should be under
        self.pathFromEnvVar = pathFromEnvVar
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return os.path.join(os.environ[self.envVar], self.pathFromEnvVar)
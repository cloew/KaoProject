import os

class Path:
    """ Represents a path to a project """
    
    def __init__(self, envVar, pathFromEnvVar, srcPath=None):
        """ Initialize the path """
        self.envVar = envVar # An Environment Variable containing a directory the Project should be under
        self.pathFromEnvVar = pathFromEnvVar
        self.srcPathFromRoot = srcPath
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return os.path.join(os.environ[self.envVar], self.pathFromEnvVar)
        
    @property
    def srcpath(self):
        """ Return the source folder path """
        if self.srcPathFromRoot is None:
            return self.filepath
        else:
            return os.path.join(self.filepath, self.srcPathFromRoot)
        
    @property
    def filepathWithEnvVar(self):
        """ Return the actual file path """
        return os.path.join("${0}".format(self.envVar), self.pathFromEnvVar)
        
    @property
    def srcpathWithEnvVar(self):
        """ Return the source folder path """
        if self.srcPathFromRoot is None:
            return self.filepathWithEnvVar
        else:
            return os.path.join(self.filepathWithEnvVar, self.srcPathFromRoot)
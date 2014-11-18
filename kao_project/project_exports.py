
class ProjectExports:
    """ Represents the project bash exports and aliases for a Project """
    
    def __init__(self, project):
        """ Initialize the Project Exports with the Project to build the exports for """
        self.project = project
    
    def getLines(self):
        """ Return the export and alias lines """
        return [self.header, self.projectDir, self.projectSrcDir, self.goToAlias]
        
    @property
    def header(self):
        """ Return the Exports header """
        return "# {0} Commands".format(self.project.name)
        
    @property
    def projectDir(self):
        """ Return the project directory """
        return 'export {0}={1}'.format(self.projectDirVar, self.filepath)
        
    @property
    def projectSrcDir(self):
        """ Return the project source directory """
        return 'export {0}={1}'.format(self.projectSrcDirVar, self.srcpath)
        
    @property
    def projectDirVar(self):
        """ Return the project directory variable """
        return '{0}_dir'.format(self.commandName)
        
    @property
    def projectSrcDirVar(self):
        """ Return the project source directory variable """
        return '{0}_src'.format(self.commandName)
        
    @property
    def goToAlias(self):
        """ Return the text for the alias command to go to this project """
        return 'alias a-{0}="cd {1}"'.format(self.commandName, self.srcpath)
        
    @property
    def commandName(self):
        """ Return the command name for the project """
        return self.project.commandName
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return self.project.path.filepathWithEnvVar
        
    @property
    def srcpath(self):
        """ Return the actual file path """
        return self.project.path.srcpathWithEnvVar

class ProjectExports:
    """ Represents the project bash exports and aliases for a Project """
    
    def __init__(self, project):
        """ Intiialize the Project Exports with the Project to build the exports for """
        self.project = project
    
    def getLines(self):
        """ Return the export and alias lines """
        return [self.header, self.goToAlias]
        
    @property
    def header(self):
        """ Return the Exports header """
        return "# {0} Commands".format(self.project.name)
        
    @property
    def goToAlias(self):
        """ Return the text for the alias command to go to this project """
        return 'alias a-{0}="cd {1}"'.format(self.commandName, self.filepath)
        
    @property
    def commandName(self):
        """ Return the command name for the project """
        return self.project.commandName
        
    @property
    def filepath(self):
        """ Return the actual file path """
        return self.project.path.filepathWithEnvVar
from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

from kao_command import RegisterCommand

class Initialize:
    """ Represents a command to initialize a project """
    command = "initialize"
    description = "Initialize a single project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('project', action='store', help='Name of the project to initialize')
        
    def run(self, arguments):
        """ Run the command """
        self.initialize(arguments.project)
        
    def initialize(self, projectName):
        """ Initialize the project """
        project = ProjectFactory.load(projectName)
        if not project.existsLocally():
            project.initialize()
        else:
            print "Project already exists locally:", projectName
    
RegisterCommand(Initialize)
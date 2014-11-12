from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

from kao_command import RegisterCommand

class Update:
    """ Represents a command to update a project """
    command = "update"
    description = "Update a single project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('project', action='store', help='Name of the project to update')
        
    def run(self, arguments):
        """ Run the command """
        self.update(arguments.project)
        
    def update(self, projectName):
        """ Update the project """
        project = ProjectFactory.load(projectName)
        project.update()
    
RegisterCommand(Update)
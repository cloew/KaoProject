from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

from kao_command import RegisterCommand

class Export:
    """ Represents a command to export the project settings """
    command = "export"
    description = "Export Project aliases"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination file for the bash export and alias file')
        
    def run(self, arguments):
        """ Run the command """
        self.write(arguments.destination)
        
    def write(self, destination):
        """ Write the file """
        projects = ProjectFactory.loadAll()
        projectExports = [ProjectExports(project) for project in projects]
        with open(destination, 'w') as file:
            projectLines = ["\n".join(project.getLines()) for project in projectExports]
            file.write("\n\n".join(projectLines))
    
RegisterCommand(Export)
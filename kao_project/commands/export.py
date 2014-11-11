from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

from kao_command import RegisterCommand

class Export:
    """ Represents a command to export the project settings """
    command = "export"
    description = "Export Project aliases"
    
    def __init__(self):
        """ Initialize with the destination file and projects """
        # path = Path('kao_lib_dir', 'KaoConsole')
        # project = Project("KaoConsole", path)
        projects = ProjectFactory.loadAll()
        self.projectExports = [ProjectExports(project) for project in projects]
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination file for the bash export and alias file')
        
    def run(self, arguments):
        """ Run the command """
        self.write(arguments.destination)
        
    def write(self, destination):
        """ Write the file """
        with open(destination, 'w') as file:
            projectLines = ["\n".join(project.getLines()) for project in self.projectExports]
            file.write("\n\n".join(projectLines))
    
RegisterCommand(Export)
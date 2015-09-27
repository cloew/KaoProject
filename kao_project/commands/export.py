from kao_command.args import Arg

from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

class Export:
    """ Represents a command to export the project settings """
    description = "Export Project aliases"
    args = [Arg('destination', action='store', help='Destination file for the bash export and alias file')]
    
    # def addArguments(self, parser):
        # """ Add arguments to the parser """
        # parser.add_argument('destination', action='store', help='Destination file for the bash export and alias file')
        
    def run(self, *, destination):
        """ Run the command """
        self.write(destination)
        
    def write(self, destination):
        """ Write the file """
        projects = ProjectFactory.loadAll()
        projectExports = [ProjectExports(project) for project in projects]
        with open(destination, 'w') as file:
            projectLines = ["\n".join(project.getLines()) for project in projectExports]
            file.write("\n\n".join(projectLines))
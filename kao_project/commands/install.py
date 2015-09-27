from kao_command.args import Arg

from ..path import Path
from ..project import Project
from ..project_exports import ProjectExports
from ..project_factory import ProjectFactory

class Install:
    """ Represents a command to install a project """
    description = "Install a single project"
    args = [Arg('project', action='store', help='Name of the project to install')]
    
    # def addArguments(self, parser):
        # """ Add arguments to the parser """
        # parser.add_argument('project', action='store', help='Name of the project to install')
        
    def run(self, *, project):
        """ Run the command """
        self.install(project)
        
    def install(self, projectName):
        """ Install the project """
        project = ProjectFactory.load(projectName)
        if not project.existsLocally():
            project.install()
        else:
            print("Project already exists locally:", projectName)
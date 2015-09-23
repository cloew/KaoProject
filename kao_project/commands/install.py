from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

class Install:
    """ Represents a command to install a project """
    description = "Install a single project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('project', action='store', help='Name of the project to install')
        
    def run(self, arguments):
        """ Run the command """
        self.install(arguments.project)
        
    def install(self, projectName):
        """ Install the project """
        project = ProjectFactory.load(projectName)
        if not project.existsLocally():
            project.install()
        else:
            print("Project already exists locally:", projectName)
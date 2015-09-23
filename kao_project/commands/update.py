from kao_project.path import Path
from kao_project.project import Project
from kao_project.project_exports import ProjectExports
from kao_project.project_factory import ProjectFactory

class Update:
    """ Represents a command to update a project """
    description = "Update a single project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('project', action='store', help='Name of the project to update')
        
    def run(self, arguments):
        """ Run the command """
        projectName = arguments.project
        if projectName != 'all':
            self.update(projectName)
        else:
            self.updateAll()
        
    def update(self, projectName):
        """ Update the project """
        project = ProjectFactory.load(projectName)
        project.update()
        
    def updateAll(self):
        """ Update all the projects """
        for project in ProjectFactory.loadAll():
            if project.existsLocally():
                project.update()
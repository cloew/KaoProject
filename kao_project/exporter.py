from kao_project.project_exports import ProjectExports

class Exporter:
    """ Represents an exporter to write several projects to a file """
    
    def __init__(self, destination, projects):
        """ Initialize with the destination file and projects """
        self.destination = destination
        self.projectExports = [ProjectExports(project) for project in projects]
        
    def write(self):
        """ Write the file """
        with open(self.destination, 'w') as file:
            projectLines = ["\n".join(project.getLines()) for project in self.projectExports]
            file.write("\n\n".join(projectLines))
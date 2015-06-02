
class Extension:
    """ Represents a project extension """
    
    def install(self, parent):
        """ Install this extension of the project """
        pass
        
    def update(self, parent):
        """ Update this extension of the project """
        pass
        
    def onChange(self, parent):
        """ Process anything needed for this extension when the project changes """
        pass
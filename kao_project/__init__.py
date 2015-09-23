from .commands import commands
from kao_command import Driver

def KaoProject(scriptName):
    return Driver(scriptName, commands)
from .path import Path
from .project import Project
from .extension.extension_factory import ExtensionFactory

from kao_factory import KeyDataBoundFactory, Factory, FieldArg
from kao_factory.Source.json_source import JsonSource

import os

PROJECTS_FILENAME = os.path.expanduser("~/.projects.json")
PathFactory = Factory(Path, FieldArg("envVar"), FieldArg("path"), srcPath=FieldArg("srcPath")])

parameters = [PrimitiveParameter("name"),
              PathFactory.LoadArg("path"),
              ExtensionFactory.LoadAllArg("extensions")]
    
ProjectFactory = KeyDataBoundFactory(Factory(Project, *parameters), JsonSource(PROJECTS_FILENAME), "name")
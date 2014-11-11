from path import Path
from project import Project

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

import os

PROJECTS_FILENAME = os.path.expanduser("~/.projects.json")
PathFactory = Factory(Path, [PrimitiveParameter("envVar"), PrimitiveParameter("path")])

parameters = [PrimitiveParameter("name"),
                    ComplexParameter("path", PathFactory.load)]
    
ProjectFactory = DataSourceFactory(Project, parameters, JsonSource(PROJECTS_FILENAME), "name")
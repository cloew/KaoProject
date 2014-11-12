from git_extension import GitExtension

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

ExtensionFactory = TypedFactory('type', {"GIT":Factory(GitExtension, [PrimitiveParameter('url')])})
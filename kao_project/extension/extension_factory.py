from .git_extension import GitExtension
from .pylib_extension import PyLibExtension

from kao_factory import TypedFactory, Factory, FieldArg

ExtensionFactory = TypedFactory('type', {"GIT":Factory(GitExtension, FieldArg('url')),
                                         "PYLIB":Factory(PyLibExtension)})
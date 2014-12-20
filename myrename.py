from rope.base.project import Project
from rope.refactor.rename import Rename

proj_dir = "code"
project = Project(proj_dir)
module = project.pycore.find_module("colors")

# Offset of the variable 'sum'
renamer = Rename(project, module, 37)
changes = renamer.get_changes("la")
project.do(changes)

# Offset of the variable 'average'
renamer = Rename(project, module, 67)
changes = renamer.get_changes("lb")
project.do(changes)

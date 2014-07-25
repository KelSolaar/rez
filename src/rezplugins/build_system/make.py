"""
Make-based build system.
"""
from rez.build_system import BuildSystem
from rez.exceptions import BuildSystemError
import os.path


class MakeBuildSystem(BuildSystem):
    @classmethod
    def name(cls):
        return "make"

    @classmethod
    def is_valid_root(cls, path):
        return os.path.isfile(os.path.join(path, "Makefile"))

    def __init__(self, working_dir, opts=None, write_build_scripts=False,
                 verbose=False, build_args=[], child_build_args=[]):
        super(MakeBuildSystem, self).__init__(working_dir)
        raise NotImplementedError


def register_plugin():
    return MakeBuildSystem

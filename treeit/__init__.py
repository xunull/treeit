import os

from .tree import Tree, TreeCmd, TreeShell


def execute_from_command_line():
    TreeShell(os.getcwd())


if __name__ == '__main__':
    pass

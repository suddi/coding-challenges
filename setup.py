import sys

# pylint: disable-msg=no-name-in-module,import-error
from distutils.cmd import Command
from os import getcwd, path
from subprocess import check_call
from setuptools import setup


class PylintCommand(Command):
    description = 'run pylint on Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['pylint', getcwd()]
        return check_call(command)

class PytestCommand(Command):
    description = 'run pytest on Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sys.path.append(path.abspath("."))
        command = ['pytest', '-c', 'test/setup.cfg']
        return check_call(command)

setup(cmdclass={
    'lint': PylintCommand,
    'test': PytestCommand
})

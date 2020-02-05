import os
import sys


class SystemInfo():
    @staticmethod
    def script_name():
        return os.path.basename(__file__)

    @staticmethod
    def python_path():
        return sys.executable

    @staticmethod
    def python_version():
        return sys.version

    @staticmethod
    def platform():
        return sys.platform

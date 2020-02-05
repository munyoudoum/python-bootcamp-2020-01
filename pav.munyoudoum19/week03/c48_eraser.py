import os
import shutil


class Eraser():
    @staticmethod
    def remove_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            return 1
        else:
            return 0

    @staticmethod
    def remove_folder(folder_name):
        if os.path.exists(folder_name):
            shutil.rmtree(folder_name)
            return 1
        else:
            return 0

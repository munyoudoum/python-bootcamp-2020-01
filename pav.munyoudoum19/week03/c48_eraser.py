import os


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
            os.rmdir(folder_name)
            return 1
        else:
            return 0


print(Eraser().remove_folder("random_folder"))
print(Eraser().remove_file("abc.txt"))

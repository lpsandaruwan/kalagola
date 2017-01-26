""" file manager

Includes functions to create/move/delete directories and files

author: Lahiru Pathirage<lpsandaruwan@gmail.com>
26/01/2017
"""

import os
import shutil


class FileManager:

    def copy_file(self, src, dest):
        shutil.copy(src, dest)

    def create_directory(self, directory_path):
        try:
            if self.is_dir_exists(directory_path):
                print(directory_path + " already exists")
            else:
                os.makedirs(directory_path)
        except:
            raise

    def is_dir_exists(self, path):
        return os.path.isdir(path)

    def is_file_exists(self, path):
        return os.path.isfile(path)

    def list_directory(self, path):
        return os.listdir(path)

    def move_directory(self, source, destination):
        shutil.move(source, destination)

    def move_file(self, file_name, dest_dir, source_file):
        try:
            shutil.move(
                source_file,
                dest_dir + "/" + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.move_file(file_name, dest_dir, source_file)

    def remove_directory(self, directory_path):
        try:
            shutil.rmtree(directory_path)
        except:
            print(
                directory_path
                + " does not exists or already has been removed"
            )

    def remove_file(self, file_path):
        os.remove(file_path)

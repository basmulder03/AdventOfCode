from collections import OrderedDict
import operator
from typing import Type

import sys, os
sys.path.append(os.path.abspath(__file__ + "/../../../common"))

from Loader import get_data

data = get_data(2022, 7)
lines = data.strip().split("\n")

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "  - {} (file, size={})".format(self.name, self.size)


class Folder:
    all_sizes = []

    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.folders = []
        self.parent = parent

    def calculate_size(self):
        file_size = sum([file.size for file in self.files])
        folder_size = sum([folder.calculate_size() for folder in self.folders])
        total_size = file_size + folder_size
        Folder.all_sizes.append(total_size)
        return total_size

    def open_or_new_folder(self, name:str):
        folders = [folder for folder in self.folders if folder.name == name]
        if len(folders) == 1:
            return folders[0]
        else:
            new = Folder(name, self)
            self.folders.append(new)
            return new

    def get_items(self):
        files = self.files
        folders = self.folders

        tree = []

        tree.extend(files)
        tree.extend(folders)

        tree.sort(key=operator.attrgetter('name'))

        return tree

    def print_tree(self, indent=0):
        items = self.get_items()
        print('  '*indent + str(self))
        for value in items:
            if type(value) == Folder:
                value.print_tree(indent+1)
            else:
                print('  '*indent + str(value))

    def __str__(self):
        return "- {} (dir)".format(self.name)


def parse():
    root = Folder("/", None)
    current_folder = root
    for line in lines:
        split = line.split(" ")
        if split[0] == '$':
            if split[1] == 'cd':
                if split[2] == '/':
                    current_folder = root
                elif split[2] == '..':
                    current_folder = current_folder.parent
                else:
                    current_folder = current_folder.open_or_new_folder(split[2])
            elif split[1] == 'ls':
                continue
        elif split[0] == 'dir':
            current_folder.open_or_new_folder(split[1])
        else:
            current_folder.files.append(File(split[1], int(split[0])))
    return root


def run1():
    root = parse()
    root.print_tree()
    Folder.all_sizes = []
    print("total size: " + str(root.calculate_size()))
    print(sum([size for size in Folder.all_sizes if size <= 100_000]))


def run2():
    root = parse()
    total_space = 70_000_000
    needed_space = 30_000_000
    Folder.all_sizes = []
    used_space = root.calculate_size()
    free_space = total_space - used_space
    space_to_free = needed_space - free_space
    print(min([size for size in Folder.all_sizes if size >= space_to_free]))




if __name__ == "__main__":
    run1()
    run2()

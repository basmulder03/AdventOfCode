with open("./dummy") as f:
    lines = f.read().split("\n")


class File:
    name: str
    size: int

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "\t- {} (file, size={})\n".format(self.name, self.size)


class Folder:
    name: str
    files: list
    folders: list

    all_sizes = []
    current_folder_path = "/"

    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def calculate_size(self):
        file_size = sum([file.size for file in self.files])
        folder_size = sum([folder.calculate_size() for folder in self.folders])
        total_size = file_size + folder_size
        Folder.all_sizes.append(total_size)
        return total_size

    def __str__(self):
        string = "- {} (dir)\n".format(self.name)
        for folder in self.folders:
            string += "\t" + str(folder)
        for file in self.files:
            string += str(file)
        return string


def run1():
    root = Folder("/")
    a = Folder("a")
    e = Folder("e")
    b = File("b.txt", 14848514)
    i = File("i", 584)
    f = File("f", 29116)
    root.folders.append(a)
    a.folders.append(e)
    e.files.append(i)
    a.files.append(f)
    root.files.append(b)
    print(root)
    # for line in lines:
    #


def run2():
    pass


if __name__ == "__main__":
    run1()
    run2()

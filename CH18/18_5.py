import os

def get_dirlist(path):
    """ Returns a sorted list of all the paths
    in a directory """

    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def r_print_files(path, prefix = ""):
    """ Recursively prints the contents of a file """

    if prefix == "":
        print("Folder listing for: " + path)
        prefix = "| "

    dirlist = get_dirlist(path)

    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            r_print_files(fullname, prefix+"| ")

def main():
    r_print_files("/Users/hjaltewallin/Documents/think_cs")


main()

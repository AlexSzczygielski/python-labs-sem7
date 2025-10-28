import os

if __name__ == "__main__":
    dir_path = "/Users/olek_szczygielski/Desktop/AGH/7_sem/python_programming/python-labs-sem7/lab3"
    #dir_path = "/dev"
    #ls = os.scandir(dir_path)
    #print(f"Number of files and folders in {dir_path} directory: ", len(ls))
    #print(ls)
    ls = os.scandir(dir_path)
    entries = []
    for entry in ls:
        if not entry.name.startswith('.'):
            entries.append(entry.name)
            print(entry.name)
print(len(entries))
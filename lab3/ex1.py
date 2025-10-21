import os

if __name__ == "__main__":
    dir_path = "/dev"
    ls = os.listdir(dir_path)
    print(f"Number of files and folders in {dir_path} directory: ", len(ls))
    #print(ls)
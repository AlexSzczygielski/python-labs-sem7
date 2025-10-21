import os

if __name__ == "__main__":
    dir_path = os.getcwd()
    print(f"Tree structure inside: {dir_path} \n|\n|\nv")

    for (root,dirs, files) in os.walk(dir_path,topdown=True):
        print("Path: ",root)
        print("Found Directories: ", dirs)
        print("Found Files: ", files)
        print("------------------  ------------------")
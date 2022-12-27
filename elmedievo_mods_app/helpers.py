import os

""" Creates a folder if it does not exist """
def create_folder(folder):
    if not os.path.isdir(folder):
        try:
            os.makedirs(folder)
            print(f"Created folder '{folder}'")
        except Exception as e:
            print(f"Could not create folder '{folder.name}'.\n  {e}")


""" Creates a file """
def create_file(file, contents):
    try:
        file = open(file, 'w')
        file.writelines(contents)
        print(f"Created file '{file.name}'")

    except Exception as e:
        print(f"Could not create file '{file}'.\n {e}")

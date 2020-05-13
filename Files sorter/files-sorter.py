import os
import shutil
from glob import glob

# FUNCTIONS

def add_extension(extension, category):
    # A loop is checking if the extension is already existing in another category:
    for category_folder, extensions in folders.items():
        if extension in extensions:
            print(
                f"This extension already exists in the '{category_folder}' folder. Remove it first to add it to another one.")
            return
    # A new category is created if it doesn't exist.
    if not folders.get(category):
        folders[category] = ()
    # The tupls is converted to a list in order to be able to append the new exension:
    category_list = list(folders[category])
    category_list.append(extension)
    folders[category] = tuple(category_list)
    print(f"The '{extension}' extension has been added to '{category}'.")


def remove_extension(extension, category=None):
    # If the category is specified...
    if category:
        # ... an if statement check if it exists:
        if folders.get(category):
            folder_list = list(folders[category])
            # If the extension is in the tuple, it is concerted to a list in order to remove it.
            if extension in folder_list:
                folder_list.remove(extension)
                folders[category] = tuple(folder_list)
                print(
                    f"The '{extension}' extension has been removed from '{category}.")
            else:
                print(f"This extension does not exist in '{category}'.")
                return
        else:
            print(f"There is not folder named '{category}'")
            return
    # If the categorie is not sepcified, a loop is going through the different cateogies of folders checking if the extension is in one of them:
    for category_folder, extensions in folders.items():
        if extension in extensions:
            # If the extension is in the tuple, it is concerted to a list in order to remove it.
            folder_list = list(folders[category_folder])
            folder_list.remove(extension)
            folders[category_folder] = tuple(folder_list)
            print(
                f"The '{extension}' extension has been removed from the '{category_folder}' folder.")
            return
    print(f"The '{extension}' extension does not exist.")

    
# VARIABLES
path = os.path.dirname(__file__)

folders = {"Applications": (".exe", ".msi"),
           "Music": (".mp3", ".wav", ".flac"),
           "Videos": (".mp4", ".mov", ".avi"),
           "Images": (".jpeg", ".jpg", ".png"),
           "Documents": (".pdf", ".txt"),
           "Books": (".epub", ".mobi"),
           "Temporary Files": (".tmp",),
           "Compressed Files": (".zip", ".rar")}

# add_extension(extension, category) # To add an extension in a new category or in an existing one.
# remove_extension(extension, category=None) # To remove a targeted extension in a category, which can be specified (or not).

files_path = os.path.join(path, "*")
files = glob(files_path, recursive=True)

for file in files:
    for category, extension in folders.items():
        if file.lower().endswith(extension):
            folder_path = os.path.join(path, category)
            os.makedirs(folder_path, exist_ok = True)
            shutil.move(file, folder_path)

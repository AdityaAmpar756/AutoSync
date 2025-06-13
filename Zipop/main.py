import os
from zipfile import ZipFile
pathidk="/home/ampar/Sync_Folder"
def Zipit(dir_detail):
    with open(dir_detail,"r") as addressbook:
        for parent_dir in addressbook:
            parent_dir=parent_dir.strip()
            with ZipFile(f"{os.path.join((pathidk),os.path.basename(parent_dir))}.zip","w") as ZIP:
                for root,dirs,files in os.walk(parent_dir):
                    for FILE in files:
                        file_path= os.path.join(root,FILE)
                        relpath= os.path.relpath(file_path, start=parent_dir)
                        ZIP.write(file_path,arcname=relpath)

if __name__ == "__main__":
    Zipit("/home/ampar/Workspace/Zipop/addresses.txt")
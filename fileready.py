from imports import *
def isfileready():
    if not os.path.exists(ID_PATH):
        file_meta = { "name":"AutoSync" , "mimeType":"application/vnd.google-apps.folder" }
        file = service.files().create( body = file_meta , fields = "id").execute()
        file_id = file.get("id")
        with open(ID_PATH , "w") as text:
            text.write(file_id)
            text.close()
        return True

    else:
        with open(ID_PATH,"r") as text:
            file_id = text.readline()
            if folder_exists(file_id):
                return True
            elif not folder_exists(file_id):
                print("Resolve errors!")
                return False

if __name__ == "__main__":
    print(isfileready())


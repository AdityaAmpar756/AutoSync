from imports import *
def upload(LOC_PATH,ID_PATH):
    with open(ID_PATH , "r") as text:
        folder_id = text.readline()
        text.close()
    
    LOC_PATH = LOC_PATH.strip() 
    with open("file_ids.txt" , "r") as text:
        nextline = text.readline()
        while not nextline == "":
            nextline=nextline.strip()
            service.files().update(fileId = nextline , body  = {"trashed":True}).execute()
            nextline = text.readline()
        text.close()
    os.remove("file_ids.txt")
    with open("file_ids.txt", "w") as text:
        for root,dirs,files in os.walk(LOC_PATH):
            for obj in files:
                file_meta = {"name":obj , "parents":[folder_id]}
                path = os.path.join(root , obj)
                file_cont = MediaFileUpload(filename=path , mimetype = "application/zip" , resumable = True)
                uploaded=service.files().create(body = file_meta , media_body = file_cont , fields = "id").execute()
                file_id = uploaded.get("id")
                text.writelines(f"{file_id}\n")
        text.close()    



        
if __name__ == "__main__":
    LOC_PATH = "/home/ampar/Sync_Folder"
    
    ID_PATH = "/home/ampar/Workspace/AutoSync/folder_id.txt"
    upload(LOC_PATH,ID_PATH)
    #service.files().update(fileId = "1ULWdpBXvk6C92GWBM2WYHlo7w6L6KUAz" , body = {"trashed":True}).execute()
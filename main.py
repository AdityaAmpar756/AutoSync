from imports import *
from quickstart import *
from upload import *
from fileready import *
from Zipop.main import *
def main():
    Zipit(DIR_DETAILS)
    tokengen()
    if isfileready():
        upload(LOC_PATH,ID_PATH)
    else:
        print("issue!!!")

if __name__ == "__main__":
    
    main()
import os
import tarfile
import hashlib


def extract_tar(tarfile_name,ext_dir = os.getcwd()):

    os.chdir(ext_dir)
    try:
        os.mkdir("extracts")
    except:
        print("Extracts folder already exists")
    
    print("Extracting file from folder : ",os.getcwd())
    
    if tarfile_name.endswith("tar.gz"):
        tar = tarfile.open(tarfile_name, "r:gz")
        os.chdir("extracts")
        tar.extractall()
        tar.close()
    elif tarfile_name.endswith("tar"):
        tar = tarfile.open(tarfile_name, "r:")
        os.chdir("extracts")
        tar.extractall()
        tar.close()
        
    print("Files Extracted in : ",os.getcwd())

def get_md5sum(file_name):
    with open(file_name, 'rb') as f:
        print(hashlib.md5(f.read()).hexdigest())
		

print(os.getcwd())

destination_filename = "tar_file_name"
download_dir = "dir_path_for_tar_file"

extract_tar(destination_filename,ext_dir = download_dir)
import requests
import os
import hashlib

def download_file_from_google_drive(id, destination, down_dir = os.getcwd()):

    os.chdir(down_dir)
    print("Current Directory : ",os.getcwd())
    
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    print("----get_confirm_token")
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    
    print("----save_response_content")

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
				
def get_md5sum(file_name):
    
    print("Checking md5sum...")
    with open(file_name, 'rb') as f:
        print("MD5 :",hashlib.md5(f.read()).hexdigest())
				

download_dir = "define_download_directory_here"


gdrive_file_id = "file_id_from_shared_link"
destination_filename = "download_file_name_userDefined"
download_file_from_google_drive(gdrive_file_id, destination_filename,down_dir = download_dir)


get_md5sum(destination_filename)
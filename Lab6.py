import requests
import hashlib
import subprocess
import os

def get_expected_sha256():
    
    hash_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    print(f"Trying to download the file ")
    
    try:
        resp_msg = requests.get(hash_url)
    except Exception as e:
        print(f"Error while trying to download the file")
        return None
    
    print(f"Response status code: {resp_msg.status_code}")
    
    if resp_msg.status_code == requests.codes.ok:
        
        file_content = resp_msg.text
        
        
        print("Downloaded file content:")
        print(file_content)
        
        
        return file_content.split()[0]  
    else:
        print("Failed to download the  file.")
        print("Response headers:", resp_msg.headers)
        print("Response content:", resp_msg.text)
    
    return None

def download_installer():
    
    installer_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    print(f"Trying to download the installer")
    
    try:
        resp_msg = requests.get(installer_url)
    except Exception as e:
        print(f"Error occurred while trying to download the installer")
        return None
    
    
    if resp_msg.status_code == requests.codes.ok:
        return resp_msg.content  
    return None
def installer_ok(installer_data, expected_sha256):

    computed_sha256 = hashlib.sha256(installer_data).hexdigest()

    return computed_sha256 == expected_sha256

def save_installer(installer_data):
    
    temp_folder = os.getenv('TEMP')
    
    
    installer_path = os.path.join(temp_folder, 'vlc-3.0.17.4-win64.exe')
    
    with open(installer_path, 'wb') as file:
        file.write(installer_data)
    
    return installer_path
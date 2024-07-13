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
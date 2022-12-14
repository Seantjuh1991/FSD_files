__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

# Versie 2.0
#GLOBAL VARIABLES
base_path  = os.getcwd()
cache_path = os.path.join(base_path, "files", "cache")
zip_file   = os.path.join(base_path, "files", "data.zip")

# 1 Clean Cache              
# De opdracht luidde dat wanneer de folder cache niet bestaat je die eerst aanmaakt. 
# Als hij wel bestaat dan leeg gooien. Je vond het raar in de vorige code dat ik hem aanmaakte echter was dat wel de opdracht. Je begint zonder cache folder namelijk.
                                    
def clean_cache():                                  
    if os.path.exists(cache_path):                  
        shutil.rmtree(cache_path)                   
        os.makedirs(cache_path)                      
    else:
        os.makedirs(cache_path)                      

#clean_cache()

#2 ZIP bestand uitpakken
def cache_zip(zip_file, extract_to):
    clean_cache()                                                                                                                   
    shutil.unpack_archive(zip_file, extract_to),     

#cache_zip(zip_file, cache_path)

#3 Bestandsnamen teruggeven van cache folder
def cached_files():
    path = os.path.abspath(cache_path)                                      
    return [entry.path for entry in os.scandir(path) if entry.is_file()]     

#print(cached_files())    

# Password vinden in alle bestanden
def find_password(cached_files):
    for item in cached_files:                        
        path = os.path.join(cache_path, item)        
        with open(path, "r") as File:               
            for line in File:                       
                if "password" in line:               
                    password = line.rstrip()        
                    return password.split(" ")[1]    

#print(find_password(cached_files()))
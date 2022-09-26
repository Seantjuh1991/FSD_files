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
                                    
def clean_cache():                                   # HANDLEIDING
    if os.path.exists(cache_path):                   # Check eerst of cache bestaat:
        shutil.rmtree(cache_path)                    # Deze functie gooit helaas ook de folder weg
        os.makedirs(cache_path)                      # Folder opnieuw toevoegen. Je kan er ook doorheen loopen maar dit is minder code en sneller. Maakt het ook leesbaarder
    else:
        os.makedirs(cache_path)                      # Als folder nog niet bestaat, aanmaken

#clean_cache()

#2 ZIP bestand uitpakken
def cache_zip(zip_file, extract_to):
    clean_cache()                                    # Folder eerst legen                                                                                  
    shutil.unpack_archive(zip_file, extract_to),     # ZIP uitpakken

#cache_zip(zip_file, cache_path)

#3 Bestandsnamen teruggeven van cache folder
def cached_files():
    path = os.path.abspath(cache_path)                                        # Absolute path ervan maken
    return [entry.path for entry in os.scandir(path) if entry.is_file()]      # Deze heb ik eerlijk gezegd mooi 'geleend' :)

#print(cached_files())    

# Password vinden in alle bestanden
def find_password(cached_files):
    for item in cached_files:                        # Per item in de cached files
        path = os.path.join(cache_path, item)        # Ieder path even in elkaar zetten
        with open(path, "r") as File:                # Bestand openen
            for line in File:                        # Alle lijnen scannen...
                if "password" in line:               # Op keyword password
                    password = line.rstrip()         # Helaas krijg je ook de line break mee waardoor WINCPY zegt dat het password fout is. Deze eraf knippen.                  
                    return password.split(" ")[1]    # De tekst na de spatie van het woord password wordt teruggegeven.

print(find_password(cached_files()))
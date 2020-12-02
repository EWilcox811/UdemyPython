import os
import shutil
import zipfile
import re
import pdb

def search_for_phone(file, regex = r"\d{3}-\d{3}-\d{4}"):
    f = open(file,mode='r')
    text = f.read()
    f.close()
    if re.search(regex, text):
        print(re.search(regex,text))
        return re.search(regex, text)
    else:
        return ''

results = []
for folder, sub_folders, files in os.walk(os.getcwd() + '\\instrucions\\extracted_content'):
    for f in files:
        full_path = folder + "\\" + f
        results.append(search_for_phone(full_path))
results
for r in results:
    if r !='':
        print(r.group())

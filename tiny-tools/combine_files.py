import os
import sys
from pathlib import Path

ext = '.sql'
remove_file = 'Create_Your_Main_Database_Objects'
def get_directory():
    return sys.argv[1]

def get_file_list(dir_path):
    files = list()
    for f in Path(dir_path).iterdir():
        if f.is_file() and f.suffix == ext:
            files.append(f)
    return files

def combine_files_in_directory(dir_path, combined_file_path):
    combined_contents = b''
    files = get_file_list(dir_path)
    files.sort(key=os.path.getmtime)

    for file_path in files:
        print(file_path)
        if remove_file in str(file_path):
            continue
        with open(file_path, 'rb') as file:
            file_name = f"\n\n\n******************{file_path.name}***************\n\n\n".encode()  # Get the file name and convert to bytes
            file_content = file.read()
            file_content = file_content.replace(b'\r', b'')
            combined_contents += file_name + file_content

    with open(combined_file_path, 'wb') as combined_file:
        combined_file.write(combined_contents)

current_dir = get_directory()
combined_file_path = current_dir + '/' + 'combined_all_files' + ext
combine_files_in_directory(current_dir, combined_file_path)

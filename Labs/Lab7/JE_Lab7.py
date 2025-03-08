import os
import hashlib
filesdictionary = {}
def menu():
    
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            
            try:
                find_duplicates(input("Enter directory to search"))
            except:
                print("no")
        if choice == 2:
            break

def find_duplicates(directory):
    # search os.walk(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file in filesdictionary:
                print(f'there are one or more duplicates in {file}')
            #print(f"checking {file} in {root}")
            file_path = os.path.join(root,file)
            #print(get_checksum(file_path))
            filesdictionary.update({file:get_checksum(file_path)})
            
    
    
            
    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    menu()
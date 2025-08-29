# This script compares two files by calculating and comparing their hash values.

import os
import hashlib

class FileHasser:
    # Initialize with file name and hashing algorithm (default is sha256)
    def __init__(self,file_name,algorithm="sha256"):
        self.file_name = file_name
        self.algorithm = algorithm
        self.hash_value = None

       # Calculate the hash of the file
    def calculate_hash(self):
        # Get the absolute path of the file
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir,self.file_name)
       
        # Create a hash object and read the file in chunks to update the hash
        hasser = hashlib.new(self.algorithm)
        with open(file_path,"rb") as f:
            # Read the file in 1KB chunks to avoid memory issues with large files
            chunk = f.read(1024)
            while chunk:
                hasser.update(chunk)
                chunk = f.read(1024)
        self.hash_value = hasser.hexdigest()
        return self.hash_value
    
    # Get the hash value, calculating it if not already done
    def get_hash(self):
        if not self.hash_value:
            return self.calculate_hash()
        return self.hash_value
    
    
class FileComparator:
    def __init__(self,file1,file2):
        # Initialize two FileHasser instances for the files to be compared
        self.file1 = FileHasser(file1)
        self.file2 = FileHasser(file2)
 
  # Compare the hash of this file with another file 
    def compare_files(self):
        hash1 = self.file1.get_hash()
        hash2 = self.file2.get_hash()
        if hash1 == hash2:
            print("Files are identical.")
        else:   
            print("Files are different.")

# Example usage
comparator = FileComparator("diff.txt","hash")
comparator.compare_files()
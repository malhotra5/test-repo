#!/usr/bin/env python3

import os
import sys
import re

def get_version_from_file(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
        # Look for version patterns like version = "x.y.z" or __version__ = "x.y.z"
        version_match = re.search(r'(?:version|__version__)\s*=\s*["\'](\d+\.\d+(?:\.\d+)?)["\']', content)
        if version_match:
            return version_match.group(1)
    return None

def main():
    # Define the target version
    target_version = "0.17"
    
    # List of files to check
    files_to_check = [
        "pyproject.toml",
        "setup.py",
        "__init__.py"
    ]
    
    inconsistent_files = []
    
    for file in files_to_check:
        version = get_version_from_file(file)
        if version and version != target_version:
            print(f"Version mismatch in {file}: found {version}, expected {target_version}")
            inconsistent_files.append(file)
    
    if inconsistent_files:
        sys.exit(1)
    else:
        print("All version numbers are consistent!")
        sys.exit(0)

if __name__ == "__main__":
    main()

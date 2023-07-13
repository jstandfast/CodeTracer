import os
import re
import source_file

class FileScanner:
    def __init__(self, path):
        self.path = path
        self.files = []

    def scan(self):
        self.files = self.get_java_files()
        # This can be fleshed out to scan for all source files

    def get_java_files(self):
        java_files = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(os.path.join(root, file))
        return java_files
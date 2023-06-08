import os
import re
import source_file

class file_scanner:
    def __init__(self, path):
        self.path = path
        self.files = []

    def full_scan(self):
        self.scan()
        source_files_objs = self.load()
        return source_files_objs

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

    def load(self):
        source_files_objs = []
        for file in self.files:
            source_files_objs.append(self.parse_file(file))
        return source_files_objs

    def parse_file(self, file_path):
        file_name = os.path.basename(file_path)
        file_title, file_type = file_name.split('.')
        lines = self.extract_lines(file_path)
        source_file_obj = source_file.source_file(file_title, file_type, lines)
        return source_file_obj

    def extract_lines(self, file_path):
        lines = {}
        with open(file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                lines[f"Line #{i}"] = line.strip()
        return lines
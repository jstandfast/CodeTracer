import sys
from file_scanner import FileScanner
from source_file import *
from file_partitioner import FilePartitioner
import java_parser_listener
# code_partitioner script
from code_tracer.store_source_files.models import LanguageModel, ProjectModel, SourceFileModel, SourceClassModel, FileClass, SourceMethodModel, ClassMethod, SourceFieldModel, ClassField, SourceParameterModel, MethodParameter


if __name__ == "__main__":

	# Testing if user input argument to represent target project path
	if len(sys.argv) > 1:
	  target_path = sys.argv[1]
	else:
	  print('No project path provided.\nRun again with path as argument.')
	  exit()

	scanner = FileScanner(target_path)
	scanner.scan()

	print(f"Scanning {len(scanner.files)} files.")

	for file in scanner.files:
		print(str(file))
		fp = FilePartitioner(file)
		java_file_x = fp.parse()
		# print(str(java_file_x))

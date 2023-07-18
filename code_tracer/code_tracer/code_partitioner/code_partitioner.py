import sys
from file_scanner import FileScanner
from source_file import *
from file_partitioner import FilePartitioner
import java_parser_listener

if __name__ == "__main__":

	# Testing if user input argument to represent target project path
	if len(sys.argv) > 1:
	  target_path = sys.argv[1]
	else:
	  print('No project path provided.\nRun again with path as argument.')
	  exit()

	scanner = FileScanner(target_path)
	scanner.scan()

	for file in scanner.files:
		# print(str(file))
		fp = FilePartitioner(file)
		java_file_x = fp.parse()
		print(str(java_file_x))

	# TODO: Change path to output
	# for seg in segments:
		# TODO: Generate each segment to an executable file with same file type as source files
		# TODO LATER: Set up a module that organizes segments into entities in a database
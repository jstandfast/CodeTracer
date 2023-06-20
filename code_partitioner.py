import sys
import file_scanner
import source_file
import java_parser_listener
# import file_partitioner
# import file_partition

if __name__ == "__main__":

	# Testing if user input argument to represent target project path
	if len(sys.argv) > 1:
	  target_path = sys.argv[1]
	else:
	  print('No project path provided.\nRun again with path as argument.')
	  exit()

	scanner = file_scanner.file_scanner(target_path)
	files_to_partition = scanner.full_scan()

	for file in files_to_partition:
		print(str(file))
		"""
		partitioner = file_partitioner(file)
		file_partitions = partitioner.partition()
		file.save_partitions(file_partitions)
		"""

	# TODO: Change path to output
	# for seg in segments:
		# TODO: Generate each segment to an executable file with same file type as source files
		# TODO LATER: Set up a module that organizes segments into entities in a database
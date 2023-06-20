class java_source_file(source_file):
	def __init__(self, file_title, file_type, lines, classes):
		self.file_title = file_title
		self.file_type = file_type
		self.lines = lines
		self.classes = classes

	def __str__(self):
		output = f"File: {self.file_title}\n"
		output += f"Lang: {self.file_type}\n"
		output += "Lines:\n"
		i = 1
		for i, line_content in self.lines.items():
    		output += f"  Line #: {i}: {line_content}\n"
		return output
import constants
from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from partitioner_java_visitor import PartitionerJavaVisitor

class FilePartitioner:
	def __init__(self, file_path):
		self.file_path = file_path
		self.file_name = self.file_path.rsplit('\\')[-1] if self.file_path is not None else None
		self.file_type = self.file_name.rsplit('.')[-1] if self.file_name is not None else None

	def parse(self):
	    if self.file_type == constants.JAVA:
	        return self.parse_java_file()


	def parse_java_file(self):
		input_stream = FileStream(self.file_path)
		lexer = JavaLexer(input_stream)
		token_stream = CommonTokenStream(lexer)
		parser = JavaParser(token_stream)
		tree = parser.compilationUnit()

		visitor = PartitionerJavaVisitor(self.file_name)
		java_file = visitor.visit(tree)

		return java_file
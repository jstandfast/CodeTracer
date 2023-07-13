from source_file import SourceFile, SourceClass, SourceMethod, SourceField, SourceParameter

class JavaFile(SourceFile):
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes  # List of JavaClass objects

class JavaClass(SourceClass):
    def __init__(self, name, methods, fields):
        super().__init__(name)
        self.methods = methods  # List of JavaMethod objects
        self.fields = fields  # List of JavaField objects

class JavaMethod(SourceMethod):
    def __init__(self, name, return_type, parameters, body):
        super().__init__(name)
        self.return_type = return_type
        self.parameters = parameters  # List of JavaParameter objects
        self.body = body  # String representing method body

class JavaField(SourceField):
    def __init__(self, name, field_type):
        super().__init__(name)
        self.field_type = field_type

class JavaParameter(SourceParameter):
    def __init__(self, name, param_type):
        super().__init__(name)
        self.param_type = param_type
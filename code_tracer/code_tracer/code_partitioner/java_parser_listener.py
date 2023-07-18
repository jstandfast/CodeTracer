from antlr4 import *
from JavaLexer import *
from JavaParser import *

class java_parser_listener():
    def __init__(self):
        self.partition = []

    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        class_name = ctx.Identifier().getText()
        modifiers = self._get_modifiers(ctx)
        methods = []
        class_info = ClassInfo(class_name, modifiers, methods)
        self.partition.append(class_info)
        print(f"Found class declaration: {class_name}")

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        method_name = ctx.Identifier().getText()
        modifiers = self._get_modifiers(ctx)
        return_type = self._get_return_type(ctx)
        parameters = self._get_parameters(ctx)
        body = self._get_method_body(ctx)
        method_info = MethodInfo(method_name, modifiers, return_type, parameters, body)
        class_info = self.partition[-1]
        class_info.methods.append(method_info)
        print(f"Found method declaration: {method_name}")

    def _get_modifiers(self, ctx):
        modifiers = []
        for modifier_ctx in ctx.modifier():
            modifiers.append(modifier_ctx.getText())
        return modifiers

    def _get_return_type(self, ctx):
        return_type_ctx = ctx.typeTypeOrVoid()
        if return_type_ctx.Void():
            return "void"
        return return_type_ctx.getText()

    def _get_parameters(self, ctx):
        parameters = []
        parameter_list_ctx = ctx.formalParameters().formalParameterList()
        if parameter_list_ctx:
            for parameter_ctx in parameter_list_ctx.formalParameter():
                parameter = parameter_ctx.variableDeclaratorId().getText()
                parameters.append(parameter)
        return parameters

    def _get_method_body(self, ctx):
        method_body_ctx = ctx.methodBody()
        if method_body_ctx:
            start_token = method_body_ctx.getStart().tokenIndex
            stop_token = method_body_ctx.getStop().tokenIndex
            return ctx.start.getInputStream().getText(start_token + 1, stop_token)
        return None

    def parse_java_code(code):
        input_stream = InputStream(code)
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()

        listener = JavaParserListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.partition
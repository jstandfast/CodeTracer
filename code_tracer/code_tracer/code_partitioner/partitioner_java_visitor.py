from antlr4 import *
from JavaParser import JavaParser
from JavaVisitor import JavaVisitor
from java_source_file import *

class PartitionerJavaVisitor(JavaVisitor):
    def __init__(self, file_name):
        self.file_name = file_name

    def visitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        # Each type declaration is either a class or an interface
        classes = [self.visit(classCtx) for classCtx in ctx.typeDeclaration() if classCtx.classDeclaration() is not None]
        return JavaFile(self.file_name, classes)

    def visitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        method_contexts = [classBodyDecl.memberDeclaration().methodDeclaration() for classBodyDecl in ctx.classBody().classBodyDeclaration() if classBodyDecl.memberDeclaration() is not None and classBodyDecl.memberDeclaration().methodDeclaration() is not None]
        methods = [self.visit(methodCtx) for methodCtx in method_contexts]
        field_contexts = [classBodyDecl.memberDeclaration().fieldDeclaration() for classBodyDecl in ctx.classBody().classBodyDeclaration() if classBodyDecl.memberDeclaration() is not None and classBodyDecl.memberDeclaration().fieldDeclaration() is not None]
        fields = [self.visit(fieldCtx) for fieldCtx in field_contexts]
        return JavaClass(ctx.Identifier().getText(), methods, fields)

    def visitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        parameter_list_context = ctx.formalParameters().formalParameterList()
        if parameter_list_context is not None:
            parameters = [self.visit(paramCtx) for paramCtx in parameter_list_context.formalParameter()]
        else:
            parameters = []
        
        # Check for None before calling getText()
        identity = ctx.Identifier().getText() if ctx.Identifier() else "void"
        type_spec = ctx.typeSpec().getText() if ctx.typeSpec() else "void"
        method_body = ctx.methodBody().getText() if ctx.methodBody() else "void"
        
        return JavaMethod(identity, type_spec, parameters, method_body)

    def visitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        return JavaField(ctx.variableDeclarators().variableDeclarator(0).variableDeclaratorId().getText(), ctx.typeSpec().getText())

    def visitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
        return JavaParameter(ctx.variableDeclaratorId().getText(), ctx.typeSpec().getText())
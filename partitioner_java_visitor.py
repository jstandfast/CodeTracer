from antlr4 import *
from JavaParser import JavaParser
from JavaVisitor import JavaVisitor

from java_source_file import *

class PartitionerJavaVisitor(JavaVisitor):
    def visitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        classes = self.visit(ctx.typeDeclaration())
        return JavaFile(ctx.fileName, classes)
    
    def visitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        methods = self.visit(ctx.methodDeclaration())
        fields = self.visit(ctx.fieldDeclaration())
        return JavaClass(ctx.Identifier().getText(), methods, fields)

    def visitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        parameters = self.visit(ctx.formalParameters())
        return JavaMethod(ctx.Identifier().getText(), ctx.typeType().getText(), parameters, ctx.methodBody().getText())

    def visitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        return JavaField(ctx.variableDeclarators().variableDeclarator(0).variableDeclaratorId().getText(), ctx.typeType().getText())

    def visitFormalParameters(self, ctx:JavaParser.FormalParametersContext):
        parameters = []
        for paramCtx in ctx.formalParameterList().formalParameter():
            parameters.append(JavaParameter(paramCtx.variableDeclaratorId().getText(), paramCtx.typeType().getText()))
        return parameters
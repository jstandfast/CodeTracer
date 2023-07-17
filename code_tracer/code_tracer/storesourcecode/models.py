from django.db import models
from django.contrib.auth.models import User

class LanguageModel(models.Model):
    name = models.CharField(max_length=200)

class ProjectModel(models.Model):
    name = models.CharField(max_length=200)
    upload_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SourceFileModel(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)

class SourceClassModel(models.Model):
    name = models.CharField(max_length=200)
    files = models.ManyToManyField(SourceFileModel, through='FileClass', related_name='classes')

class FileClass(models.Model):
    file = models.ForeignKey(SourceFileModel, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(SourceClassModel, on_delete=models.CASCADE)

class SourceMethodModel(models.Model):
    name = models.CharField(max_length=200)
    return_type = models.CharField(max_length=200)
    body = models.TextField()
    classes = models.ManyToManyField(SourceClassModel, through='ClassMethod', related_name='methods')

class ClassMethod(models.Model):
    class_obj = models.ForeignKey(SourceClassModel, on_delete=models.CASCADE)
    method = models.ForeignKey(SourceMethodModel, on_delete=models.CASCADE)

class SourceFieldModel(models.Model):
    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200)
    classes = models.ManyToManyField(SourceClassModel, through='ClassField', related_name='fields')

class ClassField(models.Model):
    class_obj = models.ForeignKey(SourceClassModel, on_delete=models.CASCADE)
    field = models.ForeignKey(SourceFieldModel, on_delete=models.CASCADE)

class SourceParameterModel(models.Model):
    name = models.CharField(max_length=200)
    param_type = models.CharField(max_length=200)
    methods = models.ManyToManyField(SourceMethodModel, through='MethodParameter', related_name='parameters')

class MethodParameter(models.Model):
    method = models.ForeignKey(SourceMethodModel, on_delete=models.CASCADE)
    parameter = models.ForeignKey(SourceParameterModel, on_delete=models.CASCADE)
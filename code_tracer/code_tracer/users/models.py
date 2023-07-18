from django.db import models
from code_tracer.store_source_code.models import ProjectModel
from code_tracer.store_source_code.models import User

# Create your models here.
class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
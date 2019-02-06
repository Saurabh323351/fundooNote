from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Notes.models import Notes
# Create your models here.

class Labels(models.Model):
    label=models.CharField(max_length=100,unique=True)
    user=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    note_id=models.ForeignKey(Notes,null=True,blank=True,on_delete=models.CASCADE)
    created_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.label

# class MapLabels(models.Model):
#     label_id=models.ForeignKey(Labels,on_delete=models.CASCADE)
#     note_id=models.ForeignKey(Notes,on_delete=models.CASCADE)
#     created_time=models.DateTimeField(default=timezone.now)

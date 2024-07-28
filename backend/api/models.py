from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class AbstractUploadedFile(models.Model):
    created = models.DateTimeField(default=timezone.now() )
    name = models.CharField(max_length=254, null=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.file.name
        self.size = self.file.size
        return super().save(**kwargs)

    def delete(self, *args, **kwargs):
        keep_file = kwargs.pop("keep_file", False)
        if keep_file:
            self.file = None
        return super().delete(*args, **kwargs)



class DrugPrescriptionFileUpload(AbstractUploadedFile):
    # patient_id = models.CharField(blank=False, max_length=20)
    file = models.FileField(blank=False, null=True, upload_to='uploaded/')
    # uploaded_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return datetime.now()
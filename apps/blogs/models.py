from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='uploads/blog')
    publish_date = models.DateField()

    def __str__(self):
        return self.title
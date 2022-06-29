from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=90)
    content = models.TextField()
    profile_pic = models.ImageField(upload_to='uploads/testimonials')

    def __str__(self):
        return self.name
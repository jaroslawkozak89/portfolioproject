from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length = 255)
    project_image = models.ImageField(upload_to='images/')
    project_link = models.CharField(max_length = 255)

    def __str__(self):
        return self.project_name

class Enquiry(models.Model):
    enquiry_email = models.CharField(max_length = 255)
    enquiry_topic = models.CharField(max_length = 255)
    enquiry_description = models.TextField()
    enquiry_date = models.DateTimeField()

    def __str__(self):
        return self.enquiry_topic

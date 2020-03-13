from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length = 255)
    blog_image = models.ImageField(upload_to = 'blogs/')
    blog_pub_date = models.DateTimeField()
    blog_text = models.TextField()

    def __str__(self):
        return self.blog_title

    def blog_pub_date_pretty(self):
        return self.blog_pub_date.strftime('%b %e %Y')

    def first_letter(self):
        return self.blog_text[0]

    def summary(self):
        return self.blog_text[1:300]+"..."

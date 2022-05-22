from django.db import models
#bblog post database
class Post(models.Model):
    srn=models.CharField(max_length=120)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=40)
    desc=models.TextField()
    slug=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.title

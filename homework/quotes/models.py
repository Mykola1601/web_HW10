from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    ctreated_at = models.DateField(auto_now_add=True)
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
   

class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    ctreated_at = models.DateField(auto_now_add=True)
    
    

















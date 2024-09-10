from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        pass
        #return True if self.published_date() <= '7' else False
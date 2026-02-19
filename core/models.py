from django.db import models

# define a data structure, which has three columns: author, content and created_at.
class Comment(models.Model):
    author = models.CharField(max_length=50, default="Anonymous")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.content[:20]}"

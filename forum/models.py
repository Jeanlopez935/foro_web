from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
<<<<<<< HEAD
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    resources = models.FileField(upload_to='resources/', blank=True, null=True)
=======
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Correct reference to custom user model
        on_delete=models.CASCADE,
        related_name='posts'
    )
    category = models.ForeignKey(  # Added category relationship
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    resources = models.FileField(upload_to='resources/%Y/%m/%d/', blank=True, null=True)
>>>>>>> 3f4b7bd0cbafc8bb7999aa9dfdbadf809cab1ba6
    draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
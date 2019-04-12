from django.db import models

# Create your models here.

class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(default='', max_length=255)
    preview_url = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.preview_url

class Posts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=400)
    content = models.CharField(default='', max_length=255)
    site_url = models.CharField(max_length=400)
    vote_total = models.IntegerField(default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # The published_date does not get assigned a date immediately
    # Only after something like a publish button has been clicked does
    # published_date get assigned a datetime

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # After creating a post go to that post's detail page
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # Since a comment needs to be approved by a superuser it does not make sense
    # to go back to a list with the comments. Instead, the person is going to go
    # back to the list of all the posts.
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(str):
        return self.text

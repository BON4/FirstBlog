from django.db import models
from django.utils import timezone
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_raiting(self):
        return (self.likes, self.dislikes)

    def as_dict(self):
        return dict(
            pk=self.pk,
            author=dict(
                id=self.author.id,
                name=self.author.name,
            ),
            title=self.title,
            content=self.content,
            date_posted=self.date_posted.isoformat(),
            likes=self.likes,
            dislikes=self.dislikes,)

# Create your models here.

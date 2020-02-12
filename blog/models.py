from django.db import models
from django.utils import timezone
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", default=None)
    dislikes = models.ManyToManyField(User, related_name="dislikes", default=None)

    def __str__(self):
        return self.title

    def like_post(self, user_id):
        user = User.objects.get(id=user_id)
        if user not in self.likes.all():
            return self.likes.add(user)

    def dislike_post(self, user_id):
        user = User.objects.get(id=user_id)
        if user not in self.dislikes.all():
            return self.dislikes.add(user)

    def get_likes_count(self):
        return self.likes.count()

    def get_dislikes_count(self):
        return self.dislikes.count()

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
            likes=self.get_likes_count(),
            dislikes=self.get_dislikes_count(),)

# Create your models here.

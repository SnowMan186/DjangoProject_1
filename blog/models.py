from django.db import models
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='previews/')
    date_created = models.DateTimeField(default=now)
    published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'

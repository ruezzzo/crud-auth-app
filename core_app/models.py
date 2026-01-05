from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор поста"
    )
    title = models.CharField(
        verbose_name="Заголовок поста",
        max_length=255
    )
    content = models.TextField("Описание")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время публикации"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]

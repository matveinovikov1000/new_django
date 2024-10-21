from django.db import models


class BlogPost(models.Model):
    """Модель записи в блог"""

    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Укажите заголовок поста",
    )
    content = models.TextField(
        verbose_name="Содержание поста", help_text="Укажите содержание поста"
    )
    preview = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображения для превью",
    )
    created_at = models.DateField(auto_now_add=True)
    publication_sign = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Пост в блоге"
        verbose_name_plural = "Посты в блоге"
        ordering = [
            "title",
            "content",
            "created_at",
            "publication_sign",
            "views_counter",
        ]

    def __str__(self):
        return self.title

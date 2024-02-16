from django.db import models
from django.utils import timezone

class File(models.Model):
    file = models.FileField(max_length=100, verbose_name="Файл", null=True)
    uploaded_at = models.DateTimeField(verbose_name="Создан", default=timezone.now)
    processed = models.BooleanField(verbose_name="Обработан", default=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


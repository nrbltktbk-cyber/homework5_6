from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тег")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Статус выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="tasks",
        verbose_name="Категория"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks", verbose_name="Теги")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title

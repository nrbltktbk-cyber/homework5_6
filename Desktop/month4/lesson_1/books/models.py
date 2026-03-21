from django.db import models

class Books(models.Model):
    name_book = models.CharField(max_length=50, verbose_name='Название книги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите обложку')
    
    CATEGORY_BOOK = (
        ('Детектив', 'Детектив'),
        ('Фантастика', 'Фантастика'),
        ('Роман', 'Роман'),
        ('Приключения', 'Приключения'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_BOOK,
                                verbose_name='Категория книги')
    url_audio_book = models.URLField(verbose_name='Ссылка на аудиокнигу')
    
    views = models.PositiveIntegerField(default=0, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name_book
    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'



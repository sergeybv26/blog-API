from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование статьи')
    text = models.CharField(max_length=1024, verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')


class Comments(models.Model):
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=450, verbose_name='Текст комментария')
    user = models.CharField(max_length=150, verbose_name='Имя пользователя')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Родитель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')


from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование статьи')
    text = models.CharField(max_length=1024, verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def get_first_comment(self):
        """Получение коментариев до третьего уровня вложенности"""
        return self.comments.select_related().filter(level__lte=3).order_by('level')\
            .values('id', 'text', 'user', 'parent', 'level')


class Comments(models.Model):
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=450, verbose_name='Текст комментария')
    user = models.CharField(max_length=150, verbose_name='Имя пользователя')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Родитель')
    parent_main = models.IntegerField(blank=True, null=True, verbose_name='id комментария 3 уровня-родителя')
    level = models.IntegerField(default=1, verbose_name='уровень вложенности комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def get_last_comment(self):
        """Получение комментариев от третьего уровня вложенности и больше"""
        return Comments.objects.filter(parent_main=self.id).order_by('parent').values('id', 'text', 'user', 'parent', 'level')


@receiver(pre_save, sender=Comments)
def comment_level_update(sender, instance, **kwargs):
    if instance.parent:
        if instance.parent.parent == instance.parent:
            instance.level = instance.parent.level
        else:
            instance.level = instance.parent.level + 1

    if instance.level == 4:
        instance.parent_main = instance.parent.id
    elif instance.level > 4:
        instance.parent_main = instance.parent.parent_main

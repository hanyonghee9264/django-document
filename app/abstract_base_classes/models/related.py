from django.db import models

__all__ = (
    'Person',
    'PhotoPost',
    'TextPost',
)


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        # 유저(Person) 입장에서
        # 자신이 특정 Post의 'author'인 경우에 해당하는 모든 PostBase객체를 참조하는 역방향 매니저 이름
        related_name='posts',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'


class TextPost(PostBase):
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name})'
from django.db import models


class User1Manager(models.Manager):
    def normal_users(self):
        # super().get_queryset()
        #  상위 클래스에서 정의한 '기본적으로' 돌려줄 QuerySet
        return super().get_queryset().filter(is_admin=False)

    def admin_users(self):
        return super().get_queryset().filter(is_admin=True)


class User1(models.Model):
    # 가능한 행동(메서드)
    # - 유저 삭제
    # - 유저 이름 바꾸기
    # - 유저를 관리자로 만들기
    name = models.CharField('이름', max_length=40)
    is_admin = models.BooleanField('관리자', default=False)

    # 이 클래스에 커스텀 매니저를 적용
    objects = User1Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Inheritance_Proxy_User1'

    def find_user(self, name):
        return User1.objects.filter(name__contains=name)


class NormalUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=False)


class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class UtilMixin(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def show_items(cls):
        # cls.__name__
        # = 'NormalUser'
        print(f'- Model({cls.__name__}) items -')
        # cls._default_manager
        # = NormalUser.objects
        for item in cls._default_manager.all():
            print(item)

    def set_name(self, new_name):
        ori_name = self.name
        self.name = new_name
        self.save()
        print('{class_name} instance name change ({ori}, {new})'.format(
            class_name=self.__class__.__name__,
            ori=ori_name,
            new=new_name,
        ))


class NormalUser(UtilMixin, User1):
    items = NormalUserManager()

    class Meta:
        proxy = True


class AdminExtraManagers(models.Model):
    items = AdminUserManager()

    class Meta:
        abstract = True


class Admin(UtilMixin, User1, AdminExtraManagers):
    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()

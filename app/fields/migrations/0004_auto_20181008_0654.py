# Generated by Django 2.1.2 on 2018-10-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0003_auto_20181008_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=60, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='S,M,L 중에 선택', max_length=1, verbose_name='셔츠 사이즈'),
        ),
        migrations.AlterField(
            model_name='person',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='좋아요'),
        ),
    ]
# Generated by Django 2.1.2 on 2018-10-18 05:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user1', models.Model),
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user1', models.Model),
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='user1',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='관리자'),
        ),
        migrations.AlterField(
            model_name='user1',
            name='name',
            field=models.CharField(max_length=40, verbose_name='이름'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-12 02:59

from django.db import migrations, models
import inheritance.multi_table.models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_table', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant1',
            name='old_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(inheritance.multi_table.models.get_removed_place), related_name='old_restaurants', related_query_name='old_restaurants', to='multi_table.Place1', verbose_name='이전에 가게가 있던 장소(건물주소)'),
        ),
    ]

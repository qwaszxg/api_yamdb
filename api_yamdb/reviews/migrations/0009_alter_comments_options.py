# Generated by Django 3.2 on 2023-04-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_merge_0004_auto_20230429_1123_0007_alter_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий к отзыву', 'verbose_name_plural': 'Комментарии к отзывам'},
        ),
    ]

# Generated by Django 2.2.16 on 2022-06-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите картинку', null=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
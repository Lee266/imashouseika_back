# Generated by Django 4.0.4 on 2022-05-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0002_rename_create_at_gallery_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='イメージ画像')),
                ('content', models.TextField(verbose_name='お知らせの詳細')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
    ]

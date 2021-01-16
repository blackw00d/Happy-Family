# Generated by Django 3.0.8 on 2021-01-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFhtml', '0005_auto_20210106_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='pay',
            field=models.TextField(choices=[('Онлайн', 'online'), ('При получении', 'offline')], default='Онлайн', verbose_name='Оплата'),
        ),
        migrations.AlterField(
            model_name='users',
            name='inst_status',
            field=models.TextField(choices=[('Подписан', 'Подписан'), ('Не подписан', 'Не подписан')], default='Не подписан', verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='users',
            name='vk_status',
            field=models.TextField(choices=[('Подписан', 'Подписан'), ('Не подписан', 'Не подписан')], default='Не подписан', verbose_name='ВКонтакте'),
        ),
    ]